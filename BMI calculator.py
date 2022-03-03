#BMI calculator

print('Welcome')

print('BMI Calculator')

while True:

    name = input("Please enter a username: ")
    
    height_m = int(input("Please enter height in metre: "))
    
    weight_kg = int(input("please enter weight in kilogram: "))

    def bmi_calculator(name, height_m, weight_kg):
        bmi = weight_kg / (height_m ** 2)
       # print("bmi: ")
        print(bmi)
        if bmi < 25:
            return name + " not overweight"
        else:
            return name + " is overweight"

    result = bmi_calculator(name, height_m, weight_kg)
    print(result)

    Exit = input('Do you wish to continue? Y/N: ').upper()
    if Exit == "N":
        print('Goodbye')
        break
    else:
        continue