from flask import Flask, render_template, session, request, redirect

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'  # Set a secret key for security purposes


@app.before_request
def before_request():
    if 'count' not in session:
        session['count'] = 0

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'add2' in request.form:
            session['count'] += 2
        elif 'reset' in request.form:
            session['count'] = 0
        else:
            session['count'] += 1
        return redirect('/')
    return render_template("index.html", count=session['count'])

@app.route('/destroy_session', methods=['POST'])
def reset():
    session['count'] = 0
    return redirect('/')

app.run(debug=True)
