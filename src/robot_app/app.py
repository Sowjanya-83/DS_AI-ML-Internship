from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/move")
def move():
    move_distance = random.randint(5, 15)
    return jsonify({
        "move": move_distance
    })

if __name__ == "__main__":
    app.run(debug=True)
