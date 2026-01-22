# Copy here code of line function from previous exercise
def triangle(size):
    # You should call function line here with proper parameters
    counter = 1
    while counter <= size:
        line(counter, "#")
        counter+=1

def line(number, text):
    if len(text) == 0:
        print("*"*number)
    elif len(text) > 1 and text[1] == "":
        print
    else:
        print(text[0]*number)
# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
