from flask import Flask, render_template
app = Flask(__name__)
@app.route('/play')
def index():
    div_content = ''
    return render_template("index.html", div_content=div_content,times=3)

@app.route('/play/<int:id>')
def index1(id):
    div_content = ''
    return render_template("main.html", div_content=div_content,times=id)


@app.route('/play/<int:id>/<color>')
def index2(color, id):
    div_content = ''
    return render_template("color.html", div_content=div_content,times=id,color=color)
    	
if __name__=="__main__":
    app.run(debug=True)
               
