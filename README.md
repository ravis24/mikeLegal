
# Email Compaign 


## Run Locally

Download the project
```
git clone https://github.com/ravis24/mikeLegal.git
```

create a Virtual environment
```bash
  python3 -m venv myvenv
```

Activate Virtual environment

```bash
  source myvenv/bin/activate
```

Install dependencies

```bash
  pip install -r requirements.txt
```

go to app 

```bash
  cd mikeLegal
```


Run local server
```bash
  python manage.py runserver
```

Run Celery Server
```bash
  celery -A mikeLegal  worker --loglevel=info
```

Run Celery Beat Server
```bash
  celery -A mikeLegal beat --loglevel=info
```
App run every day at 11:47 
```
if you want to change time go to celery.py file and change hour and minute value
```
  
API
```
    http://127.0.0.1:8000/api/add_subscriber/ - POST Method (data {email,first_name}) - to add subscriber
    http://127.0.0.1:8000/api/unsubscribe/ - POST Method (data {email}) - to unsbscribe user
```


## Acknowledgements

 - go to settings.py file and add your email and password in this  EMAIL_HOST_USER = "Your Email ID" and EMAIL_HOST_PASSWORD = "you Password"

