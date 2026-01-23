# Copy here code of line function from previous exercise and use it in your solution
def spruce(space):
    print("a spruce!")
    index = space - 1
    rows = 0
    counter = 1
    while rows < space:
        print(" "*index + "*"*counter)
        index-=1
        counter+=2
        rows+=1
    print(" "*(space-1) + "*")

spruce(5)