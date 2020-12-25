import random
from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render

from .models import Notion

def home_view(request, *args, **kwargs):
    return render(request, "pages/home.html", context={}, status=200)

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
