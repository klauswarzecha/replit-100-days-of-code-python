from flask import Flask, render_template

app = Flask(__name__, static_folder='static', template_folder='templates')


@app.route('/linktree')
def linktree():
    return render_template('linktree.html')


@app.route('/')
@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')


app.run(host='0.0.0.0', port=81)
app.run(host='0.0.0.0', debug=True)
