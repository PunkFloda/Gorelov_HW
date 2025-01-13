import codecs
import subprocess
import os
from flask import Flask, render_template, request, flash, redirect

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('main.html')


@app.route('/extract', methods=["post"])
def extract():
    user_input = request.form['txt']
    with codecs.open('./input.txt', 'w', 'utf-8') as inp:
        inp.write(str(user_input))
    command = ['./tomitaparser', 'config.proto']
    subprocess.check_output(command)
    return render_template('pretty.html')


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5005)
