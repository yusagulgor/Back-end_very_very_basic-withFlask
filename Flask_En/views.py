from flask import Blueprint, render_template ,request,jsonify,redirect,url_for

main = Blueprint("main",__name__)

@main.route("/")
def home():
    return render_template("index.html",name="yüşa")

@main.route("/profile")
def profile():
    # args = request.args
    # name = args.get('name')
    return render_template("profile.html",)

@main.route("/json")
def get_json():
    return jsonify({"name":"tim","coolness":10})

@main.route("/data")
def get_data():
    data = request.json
    return jsonify(data)

@main.route("/go-to-home")
def go_to_home():
    return redirect(url_for("main.home"))