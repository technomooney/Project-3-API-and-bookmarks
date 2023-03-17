import requests
import os
from image import Image

base_url = 'https://api.unsplash.com/search/photos?'
key = os.environ.get('UNSPLASH_KEY')


def get_image_response():
    try:
        query = {'query': 'national parks', 'page': 1, 'per_page': 10, 'orientation': 'landscape', 'client_id': key}
        response = requests.get(base_url, params=query)
        response.raise_for_status()
        data = response.json()
        return data
    except Exception as ex:
        print(ex) # TODO - Switch to log instead of print
        return ex
    

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