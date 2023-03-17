import requests
import os
from image import Image

base_url = 'https://api.unsplash.com/search/photos?'
key = os.environ.get('UNSPLASH_KEY')


def get_image_response():
    """Query UnSplash API to retrieve 10 random images and information on the creator.
    Search terms: National parks, landscape orientation, 1 page, 10 images per page.
    This function will raise an exception if an error occurs
    and return the json data if no errors occur."""
    try: 
        # Query will request images matching 'national parks'. It requests one page with 10 random images in landscape orientation using env. variable key
        query = {'query': 'national parks', 'page': 1, 'per_page': 10, 'orientation': 'landscape', 'client_id': key}
        response = requests.get(base_url, params=query)
        response.raise_for_status() # Raise exception if a client or server error occurs
        data = response.json()
        return data # Return data in json format if no errors occured during request
    except Exception as ex:
        print(ex) # TODO - Switch to log instead of print
        return ex # Return any exceptions to be handled outside the function
    

def create_image_object():

    response_data = get_image_response()
    results = response_data.get('results')

    images = []
    
    for image in results:

        image_url = image.get('urls')['regular']
        creator_name = image.get('user')['name']
        creator_link = image.get('user')['links']['self']
        image_description = image.get('description')

        new_image = Image(image_url, creator_name, creator_link, image_description)
        images.append(new_image)
        
        return images