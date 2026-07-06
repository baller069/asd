from flask import Flask, jsonify, request

asd = Flask(__name__)

@asd.route("/", methods=["GET"])
def overs():
    with open("database.txt", "w") as f:
        f.write("burn west bengal")
    return {"asd": "ds"}

@asd.route("/over", methods=["GET"])
def burn():
    return {"test": "burn"}

app = asd

if __name__ == "__main__":
    asd.run(debug=True)
