def f():    
    if a=="s" and b=="g":
        return("You Win")
    if a=="s" and b=="w":
        return("You Loose")
    if a=="s" and b=="s":
        return("Tie") 
    if a=="w" and b=="g":
        return("You Loose")
    if a=="w" and b=="s":
        return("You Win") 
    if a=="w" and b=="w":
        return("Tie")
    if a=="g" and b=="s":
        return("You Loose")
    if a=="g" and b=="w":
        return("You Win") 
    if a=="g" and b=="g":
        return("Tie")
import random
c=11
z=0
while (True):
    l=["s","w","g"]
    a=random.choice(l)
    b=input("Enter s/w/g :")
    while (True):
        c=c-1
        print(c,"Chances are left")
        c==1
        break
    if c==0:
        print(f())
        print("Game Over")
        if (a=="s" and b=="g") or (a=="w" and b=="s") or (a=="g" and b=="w"):
            print("Your score is",z+10)
            z=z+10
        if (a=="s" and b=="w") or (a=="w" and b=="g") or (a=="g" and b=="s"):
            print("Your score is",z-10)
            z=z-10
        if (a=="s" and b=="s") or (a=="w" and b=="w") or (a=="g" and b=="g"):
            print("Your score is",z)
            z=z
        break
    print(f())
    if (a=="s" and b=="g") or (a=="w" and b=="s") or (a=="g" and b=="w"):
        print("Your score is",z+10)
        z=z+10
    if (a=="s" and b=="w") or (a=="w" and b=="g") or (a=="g" and b=="s"):
        print("Your score is",z-10)
        z=z-10
    if (a=="s" and b=="s") or (a=="w" and b=="w") or (a=="g" and b=="g"):
        print("Your score is",z)
        z=z