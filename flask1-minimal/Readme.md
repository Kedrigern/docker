# Flask app in docker

Velmi jednoduchá aplikace ve Flasku v Dockeru. Vychází z kontejneru `terrillo/python3flask:latest`.

## Spuštění aplikace samostatně

```bash
FLASK_APP=app FLASK_ENV=development python3 -m flask run
```

## Spuštění Dockeru

```bash
docker build -t dockerflask .
docker run -p 3000:80 dockerflask
```

Nyní aplikace běží na: `http://localhost:3000/` (zobrazí se Hello World).

## Zdroje

- [medium.com](https://medium.com/bitcraft/dockerizing-a-python-3-flask-app-line-by-line-400aef1ded3a)