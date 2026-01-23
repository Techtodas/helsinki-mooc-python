# Write your solution here
def greatest_number(first, second, third):
    if first >= second and first >= third:
        return first
    elif second  >= third:
        return second
    return third
# You can test your function by calling it within the following block
if __name__ == "__main__":
    greatest = greatest_number(1, 1, -100)
    print(greatest)