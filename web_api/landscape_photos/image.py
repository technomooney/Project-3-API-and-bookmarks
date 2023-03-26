import jsonpickle
class Image():

    def __init__(self, image_url, creator_name, creator_link, image_description) -> None:
        self.image_url = image_url
        self.creator_name = creator_name
        self.creator_link = creator_link
        self.image_description = image_description
    
    def toJSON(self):
        return jsonpickle.encode(self)

    def __repr__(self) -> str:
        return f'Image(\'{self.image_url}\', \'{self.creator_name}\', \'{self.creator_link}\', \'{self.image_description}\')'