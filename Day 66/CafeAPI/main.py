from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import json
from random import randint
app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        dictionary={}
        for column in self.__table__.columns:
            dictionary[column.name]=getattr(self,column.name)
        return dictionary


@app.route("/")
def home():
    return render_template("index.html")
    

## HTTP GET - Read Record
# get random record
@app.route("/random")
def random():
    get_cafe=Cafe.query.get(randint(1,21))
    return jsonify(cafe=get_cafe.to_dict())
    # return render_template("index.html")


# get all records
@app.route("/all")
def all_cafes():
    get_cafes=db.session.query(Cafe).all()
    return jsonify(cafes=[cafe.to_dict() for cafe in get_cafes])

# searching cafes in a particular location
@app.route("/search")
def search_loc():
    loc=request.args.get("loc")
    cafe=db.session.query(Cafe).filter_by(location=loc).first()
    if(cafe):
        return jsonify(cafe=cafe.to_dict())
    else:
        return jsonify(error={
            "Not Found":"Sorry, we don't have a cafe at this location."
        })


## HTTP POST - Create Record
@app.route("/add",methods=["POST"])
def add_cafe():
    new_cafe=Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("loc"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("price"),
        )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={
        "success":"Cafe has been added successfully!!."
    })


## HTTP PUT/PATCH - Update Record

@app.route("/update-price/<cafe_id>", methods=["PUT"])
def update_price(cafe_id):
    new_price=request.form.get("new_price")
    cafe=Cafe.query.get(cafe_id)
    cafe.coffee_price=new_price
    if(cafe):
        db.session.commit()
        return jsonify(success="successfully updated!")
    else:
        return jsonify(error={
            "Not Found":"Sorry, cafe not found in the database!"
        })


## HTTP DELETE - Delete Record

@app.route("/report-closed/<cafe_id>",methods=["DELETE"])
def delete_cafe(cafe_id):
    api_key=request.args.get("api-key")
    if(api_key=="TopSecretAPIKey"):
        to_delete=Cafe.query.get(cafe_id)
        if(to_delete):
            db.session.delete(to_delete)
            db.session.commit()
            return jsonify(success="Cafe has been removed from the database!"),200
        else:
            return jsonify(error={"Not Found":"Sorry, cafe not found in database!"}), 404
    else:
        return jsonify(error={"Forbidden":"Sorry, Permission Denied! Please check API_KEY."}), 403

if __name__ == '__main__':
    app.run(debug=True)
