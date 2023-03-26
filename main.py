from flask import Flask, render_template, session, redirect
from scratch import test
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", image_list=test_image_data)

@app.route("/save", methods=['POST'])
def save():
    park = request.form.get('park_code')
    include_weather = request.form.get('include_weather')
    print(park, include_weather)


@app.route("/display_saved_parks")
def display_saved_parks():
    return render_template('base.html')

if __name__ == "__main__":
    app.run(debug=True)