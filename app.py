from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Lesson content
lesson = [
    "Welcome to TutorCall. Let's learn Linear Equations.",
    "A linear equation contains a variable like x.",
    "Example: 2x plus 3 equals 11.",
    "Subtract 3 from both sides. Now 2x equals 8.",
    "Divide by 2. The value of x is 4.",
    "Lesson completed. Thank you."
]

session = {
    "step": 0,
    "started": False
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/start", methods=["POST"])
def start():
    session["step"] = 0
    session["started"] = True
    return jsonify({"text": "Call connected. Press 1 to start learning."})

@app.route("/input", methods=["POST"])
def user_input():
    data = request.json
    digit = data.get("digit")

    if not session["started"]:
        return jsonify({"text": "Please start the call first."})

    if digit != "1":
        return jsonify({"text": "Press 1 to continue."})

    step = session["step"]

    if step >= len(lesson):
        return jsonify({"text": "Call ended. Thank you."})

    text = lesson[step]
    session["step"] += 1

    return jsonify({"text": text})

if __name__ == "__main__":
    app.run(debug=True)