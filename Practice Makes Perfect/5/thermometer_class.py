import random

class Thermometer:
    def __init__(self):
        self.temperature = random.uniform(34.0, 42.0)
        self.is_on = False
    def turn_off(self):
        self.is_on = False
        print('The thermometer is off.')
    def turn_on(self):
        self.is_on = True
        print('The thermometer is on.')
    def measure_temperature(self):
        self.temperature = round(random.uniform(34.0, 42.0), 1) #uniform gives floats
        if self.is_on:
            print(f'Measured temperature: {self.temperature}')
        else:
            print('Turn the thermometer on first.')
    def display_temperature(self):
        if self.is_on:
            if self.temperature >= 37 and self.temperature < 41:
                print(f'Temperature: {self.temperature} (fever)')
            elif self.temperature >= 41:
                print(f'Temperature: {self.temperature} (CRITICAL TEMPERATURE!!)')
            else:
                print(f'Temperature: {self.temperature}')
        else:
            print('Turn the thermometer on first.')
        