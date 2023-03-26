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