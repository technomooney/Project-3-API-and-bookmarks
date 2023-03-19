
class ParkWeather():
    def __init__(self,park_code:str) -> None:
        self.park_code = park_code  
        self.forecast: dict = {}