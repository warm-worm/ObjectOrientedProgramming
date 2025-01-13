# tv.py file
# class definition
class TV:
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
        self.channel_names = []
    def turn_off(self):
        self.is_on = False
    def turn_on(self):
        self.is_on = True
    def set_channels(self, channels_list):
        self.channel_names = channels_list
    def show_channels(self):
        if self.channel_names:
            print('Channel list:')
            for index, channel in enumerate(self.channel_names, 1):
                print(f'{index}. {channel}')
    def set_channel(self, new_channel_no):
        if 1<= new_channel_no <= len(self.channel_names):
            self.channel_no = new_channel_no
        else:
            print('Invalid channel number.')
    def show_status(self):
        if self.is_on:
            if self.channel_no <= len(self.channel_names):
                print(f'The TV is on, the channel number is: {self.channel_no} ({self.channel_names[self.channel_no - 1]})')
            else:
                print(f'The TV is on, but the selected channel number {self.channel_no} is out of range.')
        else:
            print('The TV is off')


