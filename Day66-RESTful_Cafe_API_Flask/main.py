from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean, func
import random

app = Flask(__name__)


# CREATE DB
class Base(DeclarativeBase):
    pass


# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record

@app.route('/random', methods=['GET'])
def random_cafe():
    total_cafes = db.session.query(func.count(Cafe.id)).scalar()
    random_id = random.randint(1, total_cafes)
    curr_cafe = db.session.execute(db.select(Cafe).where(Cafe.id == random_id)).scalar()
    curr_cafe_dict = {c.name: getattr(curr_cafe, c.name) for c in curr_cafe.__table__.columns}
    return jsonify(curr_cafe_dict)


@app.route('/all', methods=['GET'])
def all_cafe():
    all_cafes = db.session.execute(db.select(Cafe).order_by(Cafe.id)).scalars().all()

    all_cafes_dict = [{c.name: getattr(cafe, c.name) for c in cafe.__table__.columns} for cafe in all_cafes]
    return jsonify(all_cafes_dict)


@app.route('/search', methods=['GET'])
def search_cafe():
    location = request.args.get('loc')
    filtered_cafes = db.session.execute(db.select(Cafe).where(Cafe.location == location)).scalars().all()

    if filtered_cafes:
        filtered_cafes_dict = [{c.name: getattr(cafe, c.name) for c in cafe.__table__.columns} for cafe in
                               filtered_cafes]
        return jsonify(filtered_cafes_dict)
    else:
        dict = {"error":
            {
                "Not Found": "Sorry ,we don't have any cafe at that location."
            }}
        return jsonify(dict)


# HTTP POST - Create Record

@app.route('/add', methods=['POST'])
def add_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("loc"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})


# HTTP PUT/PATCH - Update Record

@app.route('/update-price/<cafe_id>', methods=['PATCH'])
def update_cafe(cafe_id):
    new_price = request.args.get('new_price')

    curr_cafe = db.session.execute(db.select(Cafe).where(Cafe.id == cafe_id)).scalar()

    if curr_cafe:
        curr_cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(success="Successfully updated the price")
    else:
        return jsonify(error={"Not Found": "Sorry a Cafe with that id was not found in the database"})


# HTTP DELETE - Delete Record

@app.route('/report-closed/<cafe_id>',methods=['DELETE'])
def delete_cafe(cafe_id):
    api_key = request.args.get('api_key')

    if api_key=='abcd':
        curr_cafe = db.session.execute(db.select(Cafe).where(Cafe.id==cafe_id)).scalar()

        if curr_cafe:
            db.session.delete(curr_cafe)
            db.session.commit()
            return jsonify(success="Entry has been successfully deleted")
        else:
            return jsonify(error={
                "Not Found":"There is no such cafe in our database"
            })
    else:
        return jsonify(error = "Sorry that's not allowed make sure you have correct api key")

if __name__ == '__main__':
    app.run(debug=True)
