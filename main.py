from flask import Flask, render_template, session, redirect, request, flash, url_for
from web_api.landscape_photos import unsplash
import dotenv, pathlib, os
import jsonpickle
from data_storage import db_interaction
from web_api.national_park import national_parks
app = Flask(__name__)

dotenv.load_dotenv(dotenv_path=pathlib.Path(".")/".env")
app.secret_key = os.getenv('SECRET_APP_KEY')
current_park_db = db_interaction.ParksDB()
@app.route("/",methods=['GET',"POST"])
def home():
    if not session.get('unsplash_images'):
        unsplash_response,error = unsplash.get_image_response()
        session['unsplash_images'] = jsonpickle.encode(unsplash.create_image_object_list(unsplash_response))
        image_list = jsonpickle.decode(session.get('unsplash_images'))
        
    else:
        image_list = jsonpickle.decode(session.get('unsplash_images'))
    
    query = request.form.get('search_query')
    if query:
        park_data_response, error = national_parks.get_parks_data(query)
        returned_park_list = national_parks.create_park_objects_list(park_data_response)
    else:
        returned_park_list=None
    return render_template("index.html", image_list=image_list, park_data = returned_park_list)

@app.route("/save", methods=['POST'])
def save():
    park_code = request.form.get('park_to_save')
    include_weather = request.form.get('include_weather_checkbox')
    park = national_parks.create_park_objects_list(national_parks.get_parks_data(park_code)[0])
    current_park_db.populate_nps_table(park[0])
    return redirect(url_for('home')) #TODO make it so they dont have to re-enter the search term

@app.route("/display_saved_parks")
def display_saved_parks():
    return render_template('base.html')

if __name__ == "__main__":
    app.run(debug=True)