###### ABOUT

Python 3.8.2<br>
Django 3.1.4

The beginnings of a simple twitter-like platform. I am following [this tutorial](https://youtu.be/f1R_bykXHGE), but will also be experimenting with other features and various ways to implement them.

###### SECRET_KEY

Be sure to generate a `SECRET_KEY` for the `settings.py` module. You can use a shell that has access to the django package to generate a `SECRET_KEY` string with:

```Python
>>>from django.core.management.utils import get_random_secret_key
>>>print(get_random_secret_key())
```

Copy and paste that string into the `SECRET_KEY` variable in `settings.py`.

###### TODO

1. Post posts
    - Create
        - Text
        - Image
    - Delete
    - RT
    - Like

2. Users
    - Register
    - Login
    - Logout
    - Profile
        - Image
        - Bio
        - Follow
        - Unfollow
        - Feed

3. Following / Followers
    - List Followers
    - List Following
