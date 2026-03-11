# WRITE YOUR SOLUTION HERE:
class ListHelper:
    @classmethod
    def greatest_frequency(cls, my_list: list):
        counts = {}
        for i in my_list:
            counts[i] = counts.get(i, 0) + 1
        return max(counts, key=counts.get)
    
    @classmethod
    def doubles(cls, my_list: list):
        counts = {}
        for i in my_list:
            counts[i] = counts.get(i, 0) + 1
        
        count_unique_numbers = 0
        for value in counts.values():
            if value >= 2:
                count_unique_numbers += 1
        return count_unique_numbers