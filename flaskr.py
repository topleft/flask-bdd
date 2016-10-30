# imports
from flask import Flask, render_template, request, \
    session, flash, redirect, url_for

# configuration
DATABASE = ''
USERNAME = 'admin'
PASSWORD = 'admin'
SECRET_KEY = 'big_secret'

app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/')
def index():
    text = "Hello, World!"
    return render_template('index.html', text=text)

@app.route('/login', methods=['GET', 'POST'])
def login():
    """User login/authentication/session management."""
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('index'))
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    """User logout/authentication/session management."""
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
