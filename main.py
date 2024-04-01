from flask import Flask , url_for, redirect, render_template, request

app = Flask(__name__)

@app.route('/', methods=["POST","GET"])
def screen1():
    if request.method == "POST":
        if request.form["button"] == "Button1":
            return redirect(url_for("screen2"))
        elif request.form["button"] == "Button2":
            return redirect(url_for("screen3"))
    return render_template('screen1.html')

@app.route('/screen2')
def screen2():
    return render_template('screen2.html')
    
@app.route('/screen3')
def screen3():
    return render_template('screen3.html')
    



if __name__ == "__main__":
    app.run(debug=True)