def palind(r):
    e = len(r) - 1
    s=0
    while s<e:
        if (r[s]!=r[e]):
            return False
        s += 1
        e += 1
        return True
    
user_input = input("Enter the elements of the tuple separated by commas: ")

r = tuple(map(int, user_input.split(',')))
if (palind(r)):
    print("The Tuple is flip flop")
else:
    print("The Tuple is not flip flop")
