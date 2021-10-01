
import random
range1=0
range2=1000
attempts=10
count=0
a=random.randint(range1,range2)
name=input("What is your name? : ")
print("Hello", name.capitalize(),"! Hope you are having a nice day!")
game=input("Would you like to play a game? Y/N")
if game=="Y":
    print("Alright! I have chosen a number between {0} and {1}".format(range1,range2))
    print("You have to guess it and I will tell if its greater or smaller than the number I have chosen")
    print("You have {} chances".format(attempts))

    for i in range(0,attempts):
        choice=int(input("Guess the number"))
        count=count+1


        if a < choice:
            print("It's Greater!!" ,"Chances left :{}".format(attempts-count))1
        elif choice<a:
            print("Its Lower! Chances left :",attempts-count)
        elif a==choice:
            print("Yayy! You got it!!")
            print("You took {} attempts".format(count))

        elif a!=choice:
            print("The number was {}".format(a))
        else:
             print("Error; Please make a valid choice!")

elif game=="N".casefold():
    print("OK! Your choice!")
else:
    print("Error; Please make a valid choice!")
exit()

