from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

asd = Flask(__name__)

databaseuri = "postgresql://postgres.vgxhtzukujlhzcxltmgf:asdisunknown%2F21@aws-0-eu-central-1.pooler.supabase.com:6543/postgres"

if databaseuri and databaseuri.startswith("postgres://"):
    databaseuri = databaseuri.replace("postgres://", "postgresql://", 1)

asd.config["SQLALCHEMY_DATABASE_URI"] = databaseuri
asd.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(asd)

class Item(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

@asd.route("/", methods=["GET"])
def overs():
    with open("database.txt", "w") as f:
        f.write("burn west bengal")
    return {"asd": "ds"}

@asd.route("/tmp", methods=["POST"])
def burn():
    try:
      database = request.get_json()
      iname = database.get("name")

      if not iname:
          return {"miguel": "iname required"}

      newi = Item(name=iname)
      
      db.session.add(newi)
      db.session.commit()

      return jsonify({
          "over": newi.id,
          "over2": newi.name
      }), 201

    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}

app = asd

if __name__ == "__main__":
    asd.run(debug=True)
