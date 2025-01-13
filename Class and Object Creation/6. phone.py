class Phone():
    def __init__(self, battery_level, screen_brightness, screen_status):
        self.battery_level = battery_level
        self.screen_brightness = screen_brightness
        self.screen_status = screen_status

    def make_call(self):
        print('Calling...')

    def send_message(self):
        print('Sending a message...')

    def charge_phone(self):
        self.battery_level = 100
        print('Phone is charging. Battery full.')

    def display_status(self):
        print(f'Battery: {self.battery_level}%')
        print(f'Screen Brightness: {self.screen_brightness}')
        print(f'Screen: {self.screen_status}')

my_phone = Phone(50, 'Low', 'On')

my_phone.display_status()
my_phone.make_call()
my_phone.send_message()
my_phone.charge_phone()
my_phone.display_status()
