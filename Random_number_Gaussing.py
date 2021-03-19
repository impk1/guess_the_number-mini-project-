import random
bot=random.randint(1,10)
print("enter the number you want bet 1 to 10")
your_choice=int(input())
if(bot>your_choice):
    print("your choiced number is less than actual")
    
elif(bot<your_choice):
    print(" your choiced number is greater  than actual  ")    

elif(bot==your_choice):
    print("right answer, hurry!")


#print("yuor choice" {your_choice})
#print("bot choice"  {bot})







