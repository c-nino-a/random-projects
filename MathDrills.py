import random

rounds=int(input("How many rounds? "))+1
print(rounds)
for i in range(rounds):
    print("----Round #", i+1,"----")
    x=random.randint(-10,10)
    y=random.randint(-10,10)
    operation=random.choice(["+","-"])
    if (operation=="+"):
        z=x+y
        print(x,"+",y)
        w=int(input())
        if (w==z):
            print("Correct!")
        else:
            print("Wrong...")
        print("Answer: ",z)
    else:
        z=x-y
        print(x,"-",y)
        w=int(input())
        if (w==z):
            print("Correct!")
        else:
            print("Wrong...")
        print("Answer: ",z)

