# tv_show.py file
# main program
import tv

def main():
    # object creation
    my_tv = tv.TV()

    channels_list = [
        "TVP1", "TVP2", "Polsat", "TVN", "Filmbox", "Discovery", "National Geographic"
    ]

    my_tv.set_channels(channels_list) #setting available channels
    my_tv.show_channels()

    print("Turn TV on")
    my_tv.turn_on()
    my_tv.show_status()

    print('Change to channel 4 (TVN)')
    my_tv.set_channel(4)
    my_tv.show_status()

    print('Change to channel 7 (National Geographic)')
    my_tv.set_channel(7)
    my_tv.show_status()

    print('Change to channel 1 (TVP1)')
    my_tv.set_channel(1)
    my_tv.show_status()

    print('Change to channel 3 (Polsat)')
    my_tv.set_channel(3)
    my_tv.show_status()

    print('Turn TV off')
    my_tv.turn_off()
    my_tv.show_status()

if __name__ == "__main__":
   main() 
