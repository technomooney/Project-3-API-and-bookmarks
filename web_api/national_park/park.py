"""These methods don't have any actual implementation yet, since the calculations will depend
on the specific data available for each park. but I can fill in the code to make these methods work 
properly for your use case. """

# The Park class has two attributes: full name and description.
class Park: 

# the __init__ method takes these attributes as parameters and initializes them for the new park object.
    def __init__(self, full_name, description, state_code, location):
        self.full_name = full_name
        self.description = description
        self.state_code = state_code
        self.location = location

    def get_visitation_rate(self, year):
        # The get_visitation_rate method takes a year as a parameter and returns the visitation rate for that year.
        
        annual_visitors = 0 
        for visitor_data in self.visitors:
            if visitor_data['year'] == year:
                annual_visitors = visitor_data['count']
                break
        
        days_open = 365 # assume park is open year-round
        visitation_rate = annual_visitors / days_open
        return visitation_rate
    
    def get_revenue(self, year):
        # The get_revenue method takes a year as a parameter and returns the revenue for that year.

        visitation_rate = self.get_visitation_rate(year)
        entry_fee = 20 # assume entry fee is $20 per person
        revenue = visitation_rate * entry_fee
        return revenue