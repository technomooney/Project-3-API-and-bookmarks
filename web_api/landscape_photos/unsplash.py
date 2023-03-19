import requests
import os
from image import Image
from pprint import pprint

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
        data_result = data.get('results')
        return data_result, None # Return data in json format if no errors occured during request
    except Exception as ex:
        return None, ex # Return any exceptions to be handled outside the function
    

def create_image_object_list(results_data):
    """This function calls the get_image_response function
    to be parsed into an image object. For each of the 10
    images on the page, it collects the image URL, creator's name,
    link to the creator's profile, and a description of the image.
    Function returns a list of 10 image objects."""
    images = [] # Empty list to be filled with 10 image objects
    
    for image in results_data: # Gather needed data from each image dictionary
        image_url = image.get('urls')['regular'] 
        creator_name = image.get('user')['name']
        creator_link = image.get('user')['links']['self']
        image_description = image.get('description')

        new_image = Image(image_url, creator_name, creator_link, image_description) # Create new image and add to list of image objects
        images.append(new_image)
        
        return images

if __name__ == '__main__':
    response, Error = get_image_response()
    images = create_image_object_list(response)
    print(images)