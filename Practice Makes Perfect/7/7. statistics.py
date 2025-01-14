class Statistics:
    def __init__(self):
        self.numbers_set = []
        self.greatest = None
        self.smallest = None
        self.mean = None
        self.median = None
    def add_to_set(self):
        number = int(input('Enter a number to add: '))
        self.numbers_set.append(number)
    def greatest_number(self):
        if self.numbers_set: #not empty
            self.greatest = max(self.numbers_set)
    def smallest_number(self):
        if self.numbers_set:
            self.smallest = min(self.numbers_set)
    def arithmetic_mean(self):
        if self.numbers_set:
            self.mean = sum(self.numbers_set) / len(self.numbers_set)
    def median_calculate(self):
        if self.numbers_set:
            self.numbers_set.sort()
            l = len(self.numbers_set)
            self.median = self.numbers_set[l // 2] if l % 2 == 1 else (self.numbers_set[l // 2 - 1] + self.numbers_set[l // 2]) / 2
    def calc_print(self):
        if not self.numbers_set:
            print('The list is empty.')
            return
        print(f'The smallest number in the array: {self.smallest}')
        print(f'The greatest number in the array: {self.greatest}')
        print(f'The arithmetic mean of numbers: {self.mean}')
        print(f'The median: {self.median}')

stats = Statistics()

stats.numbers_set = [12, 37, 6, 9, 17]

stats.greatest_number()
stats.smallest_number()
stats.arithmetic_mean()
stats.median_calculate()

stats.calc_print()