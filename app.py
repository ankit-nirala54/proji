from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/choose", methods=["POST"])
def choose():
    choice = request.form.get("choice")

    if choice == "a":
        result = "💦 YESS BABYYY ITSS SOO DEEP I LOVE ITT 💦"
    elif choice == "b":
        result = "🔥 FUCKK IT FEELS GOOOD 🔥"
    elif choice == "c":
        result = "😏 YEAAA I LOVE RIDING ON YOUUUU 😏"
    else:
        result = "❌ Invalid position, go away!"

    return render_template("result.html", result=result, choice=choice)

if __name__ == "__main__":
    app.run(debug=True)
