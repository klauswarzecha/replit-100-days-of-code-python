from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)
logged_in = False


def validate(credentials: dict) -> bool:
    """Is the user in our database and did he provide 
    the right password"""
    users = {'Marco': 'Polo', 'Mata': 'Hari', 'Nan': 'Tucket'}
    valid = all((credentials.get('username')
                 in users.keys(), credentials.get('password') == users.get(
                     credentials.get('username'))))
    return valid


@app.route('/')
def index():
    if not logged_in:
        return redirect(url_for('login'))
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    global logged_in
    if not logged_in:
        if request.method == 'POST':
            credentials = {}
            credentials['username'] = request.form.get('username')
            credentials['password'] = request.form.get('password')

            if validate(credentials):
                logged_in = True
                return redirect(url_for('index'))
            else:
                error = 'Invalid credentials'
                return render_template('login.html', error=error)
        return render_template('login.html')
    else:
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()
