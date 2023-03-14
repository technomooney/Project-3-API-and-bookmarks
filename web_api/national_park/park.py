# This code defines a Park class that has several attributes representing information about a park, such as its code, full name, description, latitude, longitude, email, phone, entrance fees, entrance passes, and operating hours.
# The class also has a method that returns a list of all the parks in the database.


# The __init__ method is the constructor of the class that initializes the first two attributes (park_code and full_name) 
# with the values provided as arguments, and sets the remaining attributes to None.

class Park():    # The park class has attributes     
    def __init__(self, park_code, full_name): # the init method initializes the first two attributes with given
        # parameters and sets the rest to None.

        self.park_code = park_code
        self.full_name = full_name
        self.description = None
        self.lat = None
        self.lon = None
        self.email = None
        self.phone = None
        self.entrance_fees = None
        self.entrance_passes =  None
        self.operating_hours = None

# he __repr__ method is a special method that returns a string representation of the object, which is useful for debugging and for generating informative error messages. In this case, 
# it returns a string that includes the full_name and park_code attributes of the park object.

    def __repr__(self): # the repr method returns a string representation of the park instance.
        return f"Park({self.full_name}, {self.park_code})"