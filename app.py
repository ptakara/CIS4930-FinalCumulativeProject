from flask import Flask, render_template, jsonify, request, redirect, session

app = Flask(__name__)
app.secret_key = "secret123"

# Health check (for Jenkins/Docker)
@app.route("/api/health/")
@app.route("/api/health")
def health():
    return jsonify({"status": "ok"}), 200

# Homepage
@app.route("/")
def home():
    return render_template("index.html")

# Question 1
@app.route("/quiz", methods=["GET", "POST"])
def q1():
    if request.method == "POST":
        session["q1"] = request.form.get("q1")
        return redirect("/question2")
    return render_template("q1.html")

# Question 2
@app.route("/question2", methods=["GET", "POST"])
def q2():
    if request.method == "POST":
        session["q2"] = request.form.get("q2")
        return redirect("/question3")
    return render_template("q2.html")
    
# Question 3
@app.route("/question3", methods=["GET", "POST"])
def q3():
    if request.method == "POST":
        session["q3"] = request.form.get("q3")
        return redirect("/question4")
    return render_template("q3.html")

# Question 4
@app.route("/question4", methods=["GET", "POST"])
def q4():
    if request.method == "POST":
        session["q4"] = request.form.get("q4")
        return redirect("/question5")
    return render_template("q4.html")
    
# Question 5
@app.route("/question5", methods=["GET", "POST"])
def q5():
    if request.method == "POST":
        session["q5"] = request.form.get("q5")
        return redirect("/result")
    return render_template("q5.html")
    
# Result
@app.route("/result")
def result():
    score = 0

    if session.get("q1", "").strip().lower() == "envelope":
        score += 1
    if session.get("q2", "").strip().lower() == "map":
        score += 1
    if session.get("q3", "").strip().lower() == "echo":
        score += 1
    if session.get("q4", "").strip().lower() == "splinter":
        score += 1
    if session.get("q5", "").strip().lower() == "dictionary":
        score += 1

    return render_template("result.html", score=score)

   
# Answers Page
@app.route("/answers")
def answers():
    return render_template("answers.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
