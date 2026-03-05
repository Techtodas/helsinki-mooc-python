# Write your solution here!
class  NumberStats:
    def __init__(self):
        self.numbers = 0
        self.count = 0

    def add_number(self, number:int):
        self.numbers += number
        self.count += 1

    def count_numbers(self):
        return self.count
    
    def get_sum(self):
        return self.numbers
    
    def average(self):
        if self.count == 0:
            return 0
        return self.numbers / self.count
    
def main():
    stats = NumberStats()
    sum_even = 0
    sum_odd = 0

    while True:
        user_input = int(input("Please type in integer numbers: "))
        if user_input == -1:
            break
        
        if user_input % 2 == 0:
            sum_even += user_input
        else:
            sum_odd += user_input

        stats.add_number(user_input)

    print(f"Sum of numbers: {stats.get_sum()}")
    print(f"Mean of numbers: {stats.average()}")
    print(f"Sum of even numbers: {sum_even}")
    print(f"Sum of odd numbers: {sum_odd}")

main()