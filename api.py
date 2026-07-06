from flask import Flask, jsonify, request

asd = Flask(__name__)

@asd.route("/over", methods=["GET"])
def burn():
    return "test"

if __name__ == "__main__":
    asd.run(debug=True)