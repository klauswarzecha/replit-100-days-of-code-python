from flask import Flask, render_template, redirect, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        dream = request.form.get('dream')
        made = request.form.get('made')
        # if dream == 'no' and made == 'chelsea':
        #     return render_template('meatbag.html', made=made)
        # elif dream == 'yes' and made != 'chelsea':
        #     return render_template('badrobot.html', made=made)
        # else:
        #     return render_template('index.html')
        return render_template('youare.html', dream=dream, made=made)
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run('localhost', debug=True)
