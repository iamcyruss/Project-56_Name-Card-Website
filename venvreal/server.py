from flask import Flask, render_template


app = Flask(__name__)


@app.route('/strata')
def strata():
    #return f"Hello world!"
    return render_template('strata.html')


@app.route('/')
def index():
    #return f"Hello world!"
    return render_template('index-simple.html')


@app.route('/git')
def git():
    #return f"Hello world!"
    return render_template('git.html')


@app.route('/identity')
def identity():
    #return f"Hello world!"
    return render_template('identity.html')


if __name__ == '__main__':
    app.run(debug=True)
