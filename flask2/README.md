# Flask app in docker

Vzorová aplikace `flaskr`, ale **zatím není v dockeru**.

1. Aktivace venv: `. venv/bin/activate`
2. Instalace flasku do venv: `pip3 install flask`
3. Nastavení proměnných pro flask:
  ```bash
  set FLASK_APP=flaskr
  set FLASK_ENV=development
  ```
4. Inicializace DB: `flask init-db`
5. Spuštění aplikace: `flask run`
6. Nyní aplikace běží na:
  - `http://127.0.0.1:8000/hello`
  - `http://127.0.0.1:8000/auth/login`
7. Po skončení deaktivace venv: `deactivate`

## Zdroje

- [oficiální tutorial](http://flask.pocoo.org/docs/1.0/tutorial/)
- [zdrojáky tutorialu](https://github.com/pallets/flask/tree/master/examples/tutorial/flaskr)