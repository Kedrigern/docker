import functools
import flask

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from flaskr.db import get_db

bp = Blueprint('solution', __name__, url_prefix='/')

def check(solution):
    return solution.upper() == "BURESICAU" or solution.upper() == "BUREŠIČAU"


@bp.route('/', methods=('GET', 'POST'))
def solve():
    if request.method == 'POST':
#        nickname = request.form['nickname']
        solution = request.form['solution1'] + request.form['solution2'] + request.form['solution3'] + request.form['solution4'] + request.form['solution5'] + request.form['solution6'] + request.form['solution7'] + request.form['solution8'] + request.form['solution9']
        db = get_db()
        error = None

        if check(solution):
            rows = db.execute(
                    'SELECT COUNT(*) FROM solution'
                    ).fetchall()
            rows = rows[0][0]
            if rows < 1000:
                cursor = db.execute(
                    'INSERT INTO solution (nickname) VALUES (?)',
                    ('nickname',)
                )
                score = cursor.lastrowid
                db.commit()
                session.clear()
                session['score'] = score
                return redirect(url_for('solution.correct'))
            else:
                return redirect(url_for('solution.correct'))
        else:
            #error = 'Dekujeme za pokus, ale  "{}" neni spravne reseni.'.format(solution)
            #flash(error)
            return redirect(url_for('solution.incorrect'))

    return render_template('solve.html')

@bp.route('/incorrect', methods=('GET',))
def incorrect():
    return render_template('incorrect.html',score=session['score'])

@bp.route('/correct', methods=('GET',))
def correct():
    return render_template('correct.html',score=session['score'])

#@bp.route('/results', methods=('GET',))
#def results():
#    db = get_db()
#    results = db.execute(
#        'SELECT id, nickname, solved'
#        ' FROM solution'
#        ' ORDER BY solved ASC'
#    ).fetchall()
#    return render_template('results.html',results=results)


