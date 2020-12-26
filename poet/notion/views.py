import random
from django.conf import settings
from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render, redirect
from django.utils.http import is_safe_url

from .models import Notion
from .forms import NotionForm

ALLOWED_HOSTS = settings.ALLOWED_HOSTS

def home_view(request, *args, **kwargs):

    return render(request, "pages/home.html", context={}, status=200)

def notion_create_view(request, *args, **kwargs):
    form = NotionForm(request.POST or None)
    next_url = request.POST.get("next") or None
    print("next_url", next_url)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        if next_url != None and is_safe_url(next_url, ALLOWED_HOSTS):
            return redirect(next_url)
        form = NotionForm()

    return render(request, "components/form.html", context={"form": form})

def notion_list_view(request, *args, **kwargs):
    objs = Notion.objects.all()
    notions_list = [{"id": x.id, "content": x.content, "likes": random.randint(0, 312)} for x in objs]

    # REST API VIEW
    data = {
        "response": notions_list
    }

    return JsonResponse(data)

def notion_detail_view(request, notion_id, *args, **kwargs):

    # REST API VIEW
    data = {
        "id": notion_id,
    }
    status = 200

    try:
        obj = Notion.objects.get(id=notion_id)
        data['content'] = obj.content
    except:
        data['message'] = "Not Found"
        status = 404

    return JsonResponse(data, status=status)
