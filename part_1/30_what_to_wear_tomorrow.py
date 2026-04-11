# Write your solution here
# Write your solution here
print("What is the weather forecast for tomorrow?")
temp = int(input("Temperature: "))
rain = input("Will it rain (yes/no): ")

if temp>20 and rain =='no':
    print("Wear jeans and a T-shirt")
    
elif temp>20 and rain == 'yes':
    print("Wear jeans and a T-shirt")
    print("Don't forget your umbrella!")
    
elif temp>10 and rain == 'no':
    print("Wear jeans and a T-shirt")
    print("I recommend a jumper as well")
    
elif temp>10 and rain == 'yes':
    print("Wear jeans and a T-shirt")
    print("I recommend a jumper as well")
    print("Don't forget your umbrella!")

elif temp>5 and rain == 'no':
    print("Wear jeans and a T-shirt")
    print("I recommend a jumper as well")
    print("Take a jacket with you")

elif temp>5 and rain == 'yes':
    print("Wear jeans and a T-shirt")
    print("I recommend a jumper as well")
    print("Take a jacket with you")
    print("Don't forget your umbrella!")

elif temp<=5 and rain == 'no':
    print("Wear jeans and a T-shirt")
    print("I recommend a jumper as well")
    print("Take a jacket with you")
    print("Make it a warm coat, actually")
    print("I think gloves are in order")

elif temp<=5 and rain == 'yes':
    print("Wear jeans and a T-shirt")
    print("I recommend a jumper as well")
    print("Take a jacket with you")
    print("Make it a warm coat, actually")
    print("I think gloves are in order")
    print("Don't forget your umbrella!")


