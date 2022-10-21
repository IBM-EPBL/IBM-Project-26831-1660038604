import random
def check_ranges(limit):
    count=1
    while count<=limit:
        c=random.choice(range(15,30,1))#random temp value
        a=random.choice(range(30,90,1))
        x,y=c,a
        print("\nCurrent Temperature: ",x,"Current Humidity: ",y)
        if x>15 and y>30:
            if x<25 and y<60 :
                print("Normal Humidity and temperature ") #between 15 to 25
            else:
                print("High Humidity and temperature detected, activating alarm circuit")#greater than 25
        else:
            print("Low Humidity and temperature")#less than 15
        count=count+1
        
#driver code to set temperature counts
limit=int(input("Required Count: "))
check_ranges(limit)
