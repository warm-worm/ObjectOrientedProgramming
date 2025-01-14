from thermometer_class import Thermometer

def main():
    #Create a thermometer:#
    thermometer = Thermometer()

    print('Turn thermometer on:')
    thermometer.turn_on()

    print('Measure temperature:')
    thermometer.measure_temperature()

    print('Display temperature:')
    thermometer.display_temperature()

    print('Turn thermometer off:')
    thermometer.turn_off()

if __name__ == "__main__":
    main()

