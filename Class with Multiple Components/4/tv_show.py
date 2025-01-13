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

    print('Display the list of available channels')
    my_tv.show_channels()

    print('Set TV channels: TVP1, TVP2, Polsat, TVN, Filmbox, Discovery')
    channels_list = ["TVP1", "TVP2", "Polsat", "TVN", "Filmbox", "Discovery"]
    my_tv.set_channels(channels_list)
    my_tv.show_channels()
    
    my_tv.show_status()

    print('Turn TV off')
    my_tv.turn_off()
    my_tv.show_status()

if __name__ == "__main__":
   main() 

# channel_names = ["TVP1", "TVP2", "Polsat", "TVN", "Filmbox", "Discovery"]