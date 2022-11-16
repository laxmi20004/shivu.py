height = float(input("Enter the height in cm: "))  
weight = float(input("Enter the weight in kg: "))  
BMI = weight / (the_height/100)**2  
print("Your Body Mass Index is", the_BMI)    
if BMI <= 18.5:  
    print("Oops! You are underweight.")  
elif BMI <= 24.9:  
    print("Awesome! You are healthy.")  
elif BMI <= 29.9:  
    print("Eee! You are over weight.")  
else:  
    print("Seesh! You are obese.")  
