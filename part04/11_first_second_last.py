# Write your solution here
def first_word(first):
    first_position = first.find(" ")
    return first[:first_position]

def second_word(second):
    first_space = second.find(" ") + 1
    second_space = second.find(" ", first_space + 1)
    if second_space == -1:
        return second[first_space:]
    return second[first_space:second_space]

def last_word(last):
    last_space = last.rfind(" ")
    return last[last_space + 1:]

# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))