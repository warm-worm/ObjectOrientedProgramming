# tv_show.py file
# main program
import tv

def main():
    # object creation
    my_tv = tv.TV()

    # object usage
    print('Create TV set')
    my_tv.show_status() #current status of the tv

    print('Turn TV on')
    my_tv.turn_on()
    my_tv.show_status()

    print('Change channel to 5')
    my_tv.set_channel(5)
    my_tv.show_status()

    print('Turn TV off')
    my_tv.turn_off()
    my_tv.show_status()

if __name__ == "__main__":
   main() 