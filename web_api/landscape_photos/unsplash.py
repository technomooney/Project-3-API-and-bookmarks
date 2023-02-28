import requests
import os

base_url = 'https://api.unsplash.com/search/photos?'
key = os.environ.get('UNSPLASH_KEY')

def main():
    """PLACEHOLDER"""


def get_image_response():
    try:
        query = {'query': 'national parks', 'page': 1, 'per_page': 10, 'orientation': 'landscape', 'client_id': key}
        response = requests.get(base_url, params=query)
        response.raise_for_status()
        data = response.json()
        return data, None
    except Exception as ex:
        print(ex) # TODO - Switch to log instead of print
        return None, ex


if __name__ == '__main__':
    main()