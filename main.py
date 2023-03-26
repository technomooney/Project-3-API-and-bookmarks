from flask import Flask, render_template, session, redirect
from web_api.landscape_photos import unsplash
import dotenv, pathlib, os
import jsonpickle
app = Flask(__name__)

dotenv.load_dotenv(dotenv_path=pathlib.Path(".")/".env")
app.secret_key = os.getenv('SECRET_APP_KEY')

@app.route("/")
def home():
    if not session.get('unsplash_images'):
        unsplash_response,error = unsplash.get_image_response()
        session['unsplash_images'] = jsonpickle.encode(unsplash.create_image_object_list(unsplash_response))
        image_list = jsonpickle.decode(session.get('unsplash_images'))
        
    else:
        image_list = jsonpickle.decode(session.get('unsplash_images'))

    return render_template("index.html", image_list=image_list)

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