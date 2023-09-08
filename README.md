
# Email Compaign 


## Run Locally

Download the project
```
https://github.com/ravis24/mikeLegal.git
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

API
```
    http://127.0.0.1:8000/api/add_subscriber/
    http://127.0.0.1:8000/api/unsubscribe/
```


## Acknowledgements

 - go to settings.py file and add your email and password in this  EMAIL_HOST_USER = "Your Email ID" and EMAIL_HOST_PASSWORD = "you Password"

