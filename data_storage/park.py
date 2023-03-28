
class Park:
    def __init__(self, name, description, state_code, latitude, longitude, park_code, phone, email):
        self.name =  name
        self.description = description
        self.state_code = state_code
        self.latitude = latitude
        self.longitude = longitude
        self.park_code = park_code
        self.phone = phone
        self.email = email

    def __repr__(self) -> str:
        return f'''Name: {self.name}
        Description: {self.description}
        State Code: {self.state_code}
        Latitude: {self.latitude}, Longitude: {self.longitude} 
        Park Code: {self.park_code}
        Contact Number: {self.phone}
        Contact Email: {self.email})'''
