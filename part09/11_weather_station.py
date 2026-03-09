# WRITE YOUR SOLUTION HERE:
class WeatherStation:

    def __init__(self, station: str):
        self.__station = station
        self.__weather = []

    
    def add_observation(self, observation: str):
        self.__weather.append(observation)


    def latest_observation(self):
        if self.__weather:
            return self.__weather[-1]
        else:
            return None


    def number_of_observations(self):
        return len(self.__weather)


    def __str__(self):
        return f"{self.__station}, {self.number_of_observations()} observations"
    