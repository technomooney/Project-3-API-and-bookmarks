from landscape_photos import unsplash
from national_park import national_parks
from open_weather import open_weather_map

def get_unsplash_image_list():
    """This function calls the API request function from unsplash.py.
    The request function either returns a response or an exception;
    if there's an error, it will be logged, else, the create image object
    list function is called and the list of image objects is returned."""
    response, error = unsplash.get_image_response() # Call unsplash function to get response or exception, depending on whether the request is successful

    if error:
        print(f'An error has occured: {error}') # TODO - switch to log instead of print
    else: 
        image_list = unsplash.create_image_object_list(response) # Get image list from unsplash function if request is successful
        return image_list


def get_national_park_list(search_query):
    """This function calls the API request function from national_parks.py with 
    a search query entered by the user on the web app.
    The request function either returns a response or an exception;
    if there's an error, it will be logged, else, the create park object
    list function is called and the list of park objects is returned."""
    response, error = national_parks.get_parks_data(search_query)

    if error:
        print(f'An error has occured: {error}') # TODO - switch to log instead of print
    else: 
        parks_list = national_parks.create_park_objects_list(response) # Get parks list from national_parks function if request is successful
        return parks_list