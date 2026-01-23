# Write your solution here
def same_chars(string, first_index, second_index):

    if first_index > len(string) or second_index >= len(string):
        return False
    else:
        if string[first_index] == string[second_index]:
            return True
        return False

    
    
        
# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("abcc", 144, 77))