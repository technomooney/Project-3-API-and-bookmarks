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

    def __repr__(self): # the repr method returns a string representation of the park instance.
        return f"Park({self.full_name}, {self.park_code})"