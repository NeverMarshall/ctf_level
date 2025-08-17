from flask import Flask, request, abort
import os

app = Flask(__name__)
BASE_DIR = "/app/files"

@app.route("/")
def index():
    filename = request.args.get("file")
    if not filename:
        return "Keep ?file=<File name>"
    
    filepath = os.psth.join(BASE_DIR, filename)

    try:
        with open(filepath, "r") as f:
            return f.read()

    except:
        abort(404)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8004)
