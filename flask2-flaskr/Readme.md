# Flask app in docker

Velmi aplikace Flaskr (tutorial) ve Flasku v Dockeru. Vychází z kontejneru `terrillo/python3flask:latest`.

## Spuštění aplikace samostatně

```bash
set FLASK_APP=
set FLASK_ENV=development
python3 -m flask run
```

## Spuštění Dockeru

```bash
docker build -t dockerflask .
docker run -p 3000:80 dockerflask
```

- [Source medium.com](https://medium.com/bitcraft/dockerizing-a-python-3-flask-app-line-by-line-400aef1ded3a)
