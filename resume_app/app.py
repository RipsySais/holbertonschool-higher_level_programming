from flask import Flask, request, render_template,

app = flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.form["texte"]
        return render_template("index.html")
    return f"texte reçu : {text}"

if __name__ == "__main__":
    app.run("debug=True, host=")
