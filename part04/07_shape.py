# Copy here code of line function from previous exercise and use it in your solution
def shape(size1, triangle, size2, square):
    counter = 1
    while counter <= size1:
        line(counter, triangle)
        counter+=1

    counter2 = 1
    while counter2 <= size2:
        line(size1, square)
        counter2+=1

def line(number, text):
    if len(text) == 0:
        print("*"*number)
    elif len(text) > 1 and text[1] == "":
        print
    else:
        print(text[0]*number)
# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 3, "*")