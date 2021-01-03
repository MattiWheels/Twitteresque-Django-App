###### About

Python 3.8.2<br>
Django 3.1.4

The beginnings of a simple twitter-like platform. I am following [this tutorial](https://youtu.be/f1R_bykXHGE), but will also be experimenting with other features and various ways to implement them.

###### Installation

- Install Python and Git
- Clone repo from cmd or terminal: `git clone https://github.com/MattiWheels/Twitteresque-Django-App`
- Navigate into the project folder: `cd Twitteresque-Django-App`
- Set up a virtual environment to consolidate packages: `python -m venv venv`
- Activate virtual environment: `venv\Scripts\activate` or `source venv/bin/activate` on Unix based systems
- Install the required packages: `pip install -r requirements.txt`
- Update the `SECRET_KEY` variable to have a random string of characters (fine for testing purposes)
- Be sure to create necessary database files by navigating to mysite (`cd mysite`) and running the following bash commands: `python manage.py makemigrations` followed by `python manage.py migrate`

###### Todo

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
