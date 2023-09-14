from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/4')
def index1():
    return render_template("main.html")


@app.route('/<int:id1>/<int:id2>')
def index2(id1, id2):
    return render_template("num.html", id1=id1,id2=id2)

if __name__=="__main__":
    app.run(debug=True)
               