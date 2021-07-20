# Sup dear!

This is a project to add unlimeted contacts and use online, but, It doesn't deploy online just on the localhost. Below, the screen's and how can you use.

## Smart Contacts book screen's


![](https://github.com/guirlviana/Smart-Contacts-book/blob/main/prints/login.PNG?raw=true "Optional Title")
![](https://github.com/guirlviana/Smart-Contacts-book/blob/main/prints/dashboard.PNG?raw=true "Optional Title")
![](https://github.com/guirlviana/Smart-Contacts-book/blob/main/prints/contacts.PNG?raw=true "Optional Title")
![](https://github.com/guirlviana/Smart-Contacts-book/blob/main/prints/register.PNG?raw=true "Optional Title")

## First Step

Install dependencies project, find in requirements.txt


Change your mysql instance and schema values in the projetoAgenda/settings.py

    DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.mysql', # don't change this
    'NAME': 'agendadb',
    'HOST': '127.0.0.1',
    'PORT': '3306',
    'USER': 'root',
    'PASSWORD': PASSWORD,
    }
    }

Run the command 

    python manage.py migrate

Now, set a superuser for your project, run the command and set your profile

    python manage.py createsuperuser



## See the application

Run the command:

    python manage.py runserver

Verify the deployment by navigating to your server address in
your preferred browser.

```sh
127.0.0.1:8000
```
