
class Park:
    def __init__(self, name, description, state_code, location, park_code, phone, email):
        self.name =  name
        self.description = description
        self.state_code = state_code
        self.location = location
        self.park_code = park_code
        self.phone = phone
        self.email = email

    def __repr__(self) -> str:
        return f'\nPark({self.name} {self.description} {self.state_code} {self.location} {self.park_code} {self.phone} {self.email})'