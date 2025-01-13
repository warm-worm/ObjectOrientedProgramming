class TaxiRide:
    def __init__(self, rate_per_km):
        self.rate_per_km = rate_per_km # value in € (e.g. €2)
        self.distance = 0
        self.fare = 0

    def calculate_fare(self, distance):
        self.distance = distance
        self.fare = self.distance * self.rate_per_km

    def print_receipt(self):
        print(f'Receipt:')
        print(f'Distance: {self.distance}km.')
        print(f'Rate: {self.rate_per_km}€/km.')
        print(f'Fare: {self.fare}€.')

def main():
    # your program
    ride1 = TaxiRide(2) #2 euro per km
    ride2 = TaxiRide(4) #4 euro per km, tough luck
    ride1.calculate_fare(10) #10km
    ride2.calculate_fare(5)
    ride1.print_receipt()
    print('--------------')
    ride2.print_receipt()

if __name__ == "__main__": #ensures that its not an import module program
    main()
