Python 3.8.2

Django 3.1.4

The beginnings of a simple twitter-like platform. Following [this tutorial](https://youtu.be/f1R_bykXHGE), but will be experimenting with other features and the various ways to implement them.

###### SECRET_KEY

Be sure to generate a `SECRET_KEY` for the `settings.py` file. You can use a shell that has access to the django package to generate a `SECRET_KEY` string with:

```Python
>>>from django.core.management.utils import get_random_secret_key
>>>print(get_random_secret_key())
```

Copy and paste that string into the `SECRET_KEY` variable in `settings.py`.

###### Todo

1. Post posts
    - Create
        - Text
        - Image
    - Delete
    - RT

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
