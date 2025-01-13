# tv.py file
# class definition
class TV:
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
    def turn_off(self):
        self.is_on = False
    def turn_on(self):
        self.is_on = True
    def channel_no(self, channel):
        self.channel_no = channel
    def show_status(self):
        if self.is_on:
            print(f'The TV is on, the channel number is: {self.channel_no}')
        else:
            print('The TV is off')


