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

    print('Increase volume by 4') #because.
    for _ in range(4): 
        my_tv.increase_volume()
    my_tv.show_status()

    print('Increase volume again')
    my_tv.increase_volume()
    my_tv.show_status()

    print('Decrease volume')
    my_tv.decrease_volume()
    my_tv.show_status()

    print('Turn TV off')
    my_tv.turn_off()
    my_tv.show_status()

if __name__ == "__main__":
   main() 
