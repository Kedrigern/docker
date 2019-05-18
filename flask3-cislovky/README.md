
# Flask app in docker with DB

Dockerized Flask 1 app in Python 3 with SQLite.

Python version: 3.7
Flask version: 1.0.2
DockerImage: [tiangolo/meinheld-gunicorn-flask](https://github.com/tiangolo/meinheld-gunicorn-flask-docker)
Aplikace: [číslovky](https://github.com/Kedrigern/example-projects/tree/master/python/flask)

## Run

Build image: `docker build -t cislovky .`

Ve Fedoře je ještě třeba vypnout selinux: `sudo /sbin/setenforce 0`

Run image: `docker run --name cislovky -v "$PWD/instance:/app/instance:rw" -p 80:80 --rm cislovky`

## Anatomy

```
.
├── app
│   ├── cislovky
│   │   ├── db.py
│   │   ├── home.py
│   │   ├── __init__.py
│   │   ├── schema.sql
│   │   ├── static
│   │   │   └── style.css
│   │   └── templates
│   │       ├── base.html
│   │       └── home
│   │           ├── all.html
│   │           ├── cs.html
│   │           ├── en.html
│   │           └── home.html
│   ├── main.py
│   └── requirements.txt
├── cislovky.sqlite
├── Dockerfile
└── README.md
```

`main.py` is entrypoint:

```python3
from cislovky import create_app

app = create_app()
```