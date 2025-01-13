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
    def set_channel(self, new_channel_no):
        self.channel_no = new_channel_no
    def show_status(self):
        if self.is_on:
            print(f'The TV is on, the channel number is: {self.channel_no}')
        else:
            print('The TV is off')


