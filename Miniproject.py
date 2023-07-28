name = input("Enter your name")
height = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kg: "))

BMI = weight / (height/100)**2

print("Your BMI is", BMI)

if BMI <= 18.4:
    print(name+", you are underweight. The last three or four reps is what makes the muscle grow. This area of pain divides a champion from someone who is not a champion. So, you need to put on some weight")

elif BMI <= 24.9: 
    print(name+", you are healthy. Health is the greatest gift, contentment the greatest wealth, faithfulness the best relationship. Be healthy always")

elif BMI <= 29.9:
    print(name+", you are over weight. Every step is progress, no matter how small. Moral oft the story is lose some weight")

elif BMI <= 34.9: 
    print(name+", you are severely over weight. Excuses don’t burn calories. Moral oft the story is lose some weight")

elif BMI <= 39.9:
    print(name+", you are obese. A year from now, you will wish you started today. Moral oft the story is lose some weight")

elif BMI >= 40:
    print(name+", you are severely obese. It’s not a diet change, it’s a lifestyle change.Moral oft the story is lose some weight" )
