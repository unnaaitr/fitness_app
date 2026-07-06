# FITNESS APP BUILT WITH PYTHON


# This app will be using Mifflin-St Jeor equation to calculate the Basal Metabolic Rate
# It's the most common formula used to estimate the number of calories burned at rest, based on some variables


def variables(): # we define gender, age, weight and height from every user
    while True:
        gender = input("Please, enter your gender (male/female): ").strip().lower()

        if gender in ["male", "female"]:
            print(f"You're a {gender}\n")
            break

        else:
            print("Choose between male or female\n")

    while True:
        age = int(input("Please, enter your age: "))

        if age < 14 or age > 90:
            print("Age must be between 14 and 90 years old\n")

        else:
            print(f"You're {age:.0f} years old\n")
            break

    while True:
        weight = float(input("Please, enter your weight in kg: "))

        if weight < 30 or weight > 300:
            print("Weight must be between 30 and 300 kg\n")

        else:
            print(f"You're weighted {weight:.1f} kg\n")
            break         
            
    while True:    
        height = float(input("Please, enter you height in cm: "))

        if height < 70 or height > 250:
            print("Height must be between 70 and 250 cm\n")
                    
        else:
            print(f"You're {height:.1f} cm tall\n")
            break

    return(gender, age, weight, height)


def bmr(gender, age, weight, height): # basal metabolism
    if gender == "male":
        bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5

    elif gender == "female":
        bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161

    else:
        print("Choose between male or female\n")

    return bmr


# that's an important thing for having the result of the variables
gender, age, weight, height = variables()
result = bmr(gender, age, weight, height)
print(f"Your BMR is {result:.0f} calories")