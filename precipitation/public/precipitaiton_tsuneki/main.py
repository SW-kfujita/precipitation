from flask import Flask, render_template, request
import random
app = Flask(__name__)

@app.route("/")
def index():
    start = request.args.get("start", "")
    average = random.randint(0, 100)
    return render_template("index.html",
                            start=start,
                            average=average)

if __name__ == '__main__':
    app.run( host = '0.0.0.0' )