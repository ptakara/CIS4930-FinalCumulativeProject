from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

@app.route("/health")
def health():
    return jsonify({"status": "ok"}), 200

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/quiz")
def quiz():
    return render_template("quiz.html")

@app.route("/result", methods=["POST"])
def result():
    q1 = request.form.get("q1")
    q2 = request.form.get("q2")

    score = 0

    if q1 == "C":
        score += 1

    if q2 == "B":
        score += 1

    return render_template("result.html", score=score)
   

    
if __name__ == "__main__":
    app.run(debug=True)
