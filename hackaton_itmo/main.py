from flask import Flask, render_template, request

import parcer as p

app = Flask(__name__, static_folder="static")


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        print(text)
        vacs = p.hh_ru(text)
        print(vacs)
        return render_template('table.html', list_a=vacs)
    else:
        return render_template('index.html')


@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        text = request.form['text']
        print(text)
        vacs = p.hh_ru(text)
        print(vacs)
        return render_template('table.html', list_a=vacs)
    else:
        return render_template('table.html')


if __name__ == '__main__':
    app.run()
