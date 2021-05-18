import flask
import mod_simple_ferm
from flask import Flask, request

app = Flask(__name__, static_folder="static", static_url_path="", template_folder="templates")


@app.route('/')
def root():
    return flask.render_template(
        'index.html'
    )


@app.route('/test')
def is_simple_ferm():
    if request.method == 'GET':
        n=request.args.get('name_n')
        count=request.args.get('name_count')
    if (n != None) and (count != None):
        n = int(n)
        count = int(count)
        n = mod_simple_ferm.is_simple_ferm(n, count)
        if n == False:
            n = 'Число составное'
        else:
            n = 'Число простое'
    return flask.render_template('test.html', name = n)

if __name__ == '__main__':
   app.run(debug = True)