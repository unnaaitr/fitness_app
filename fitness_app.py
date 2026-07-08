# FITNESS APP BUILT WITH PYTHON


# This app will be using Mifflin-St Jeor equation to calculate the Basal Metabolic Rate
# It's the most common formula used to estimate the number of calories burned at rest, based on some variables


# Before anything, we need to know what BMR and TDEE are:
    # BMR = Basal Metabolic Rate (calories your body burns at complete rest)
    # TDEE = Total Daily Energy Expenditure (total calories you burn per day including physical activity)
        # To calculate TDEE, we need to multiply BMR by the activity factor


def variables(): # We define gender, age, weight and height from every user
    while True:
        gender = input("Please, enter your gender (male/female): ").strip().lower()

        if gender in ["male", "female"]:
            print(f"- You're a {gender}\n")
            break

        else:
            print("Please, choose between male or female\n")

    while True:
        age = int(input("Please, enter your age: "))

        if age < 14 or age > 90:
            print("Age must be between 14 and 90 years old\n")

        else:
            print(f"- You're {age:.0f} years old\n")
            break

    while True:
        weight = float(input("Please, enter your weight in kg: "))

        if weight < 30 or weight > 300:
            print("Weight must be between 30 and 300 kg\n")

        else:
            print(f"- You're weighted {weight:.1f} kg\n")
            break         
            
    while True:    
        height = float(input("Please, enter you height in cm: "))

        if height < 70 or height > 250:
            print("Height must be between 70 and 250 cm\n")
                    
        else:
            print(f"- You're {height:.1f} cm tall\n")
            break

    return(gender, age, weight, height)


def bmr(gender, age, weight, height): # Basal Metabolism Rate (different between men and women)
    if gender == "male":
        bmr_calc = (10 * weight) + (6.25 * height) - (5 * age) + 5

    elif gender == "female":
        bmr_calc = (10 * weight) + (6.25 * height) - (5 * age) - 161

    else:
        print("Please, choose between male or female\n")

    return bmr_calc


def tdee(bmr_calc): # Then we have to add the activity factor
    while True:
        activity_factor = int(input("Please, select your activity level:\n1 - Sedentary (office job, no exercise)\n2 - Light (1-3 days of exercise per week)\n3 - Moderate (3-5 days of exercise per week)\n4 - Intense (6-7 days of exercise per week)\n5 - Athlete (physical job + daily training)\n\nChoose (1-5): "))

        if activity_factor == 1:
            print("- You're sedentary")
            tdee_calc = bmr_calc * 1.2
            break

        elif activity_factor == 2:
            print("- You have a light activity level")
            tdee_calc = bmr_calc * 1.375
            break

        elif activity_factor == 3:
            print("- You have a moderate activity level")
            tdee_calc = bmr_calc * 1.55
            break

        elif activity_factor == 4:
            print("- You have an intense activity level")
            tdee_calc = bmr_calc * 1.725
            break

        elif activity_factor == 5:
            print("- You're an athlete")
            tdee_calc = bmr_calc * 1.9
            break

        else:
            print("Please, choose a correct option (1-5)")

    return tdee_calc


# We will calculate the BMI (Body Mass Index) and offer the user a recommendation that can be accepted or not, and then it will show what to do if it's not liked
def bmi(height, weight):
    print("Now it will be shown a recommendation based on your height and weight")

    bmi_calc = weight / (height / 100) ** 2

    if bmi_calc < 18.5:
        to_do = "bulk"
        print("- You're underweighted, you should bulk\n")

    elif bmi_calc < 24.9:
        to_do = "mantain"
        print("- You're okay, you should maintain your bodyweight\n")

    elif bmi_calc < 29.9:
        to_do = "cut"
        print("- You're overweighted, you should cut\n")

    else:
        to_do = "cut"
        print("- You're obese, you should cut\n")


    # We're now doing if the user wants to do the recommendation or not
    while True:
        approval = input("Do you like the recommendation (yes/no): ").strip().lower()

        if approval == "yes":
            print(f"- You have choosen to {to_do}")
            break

        elif approval == "no":
            while True:       
                new_choose = input("What do you want to do (bulk, mantain, cut) weight? ")

                if new_choose == "bulk":
                    to_do = new_choose
                    print(f"- You have choosen to {new_choose}\n")
                    break 

                elif new_choose == "mantain":
                    to_do = new_choose
                    print(f"- You have choosen to {new_choose}\n")
                    break
            
                elif new_choose == "cut":
                    to_do = new_choose
                    print(f"- You have choosen to {new_choose}\n")
                    break
        
                else:
                    print("Please, choose a correct option")

            break # If we don't use it, the loop continues

        else:
            print("Please, choose a correct option")

    return bmi_calc, to_do


def macros(tdee_calc, weight, to_do): # This function will calculate calories, protein, fat and carbs for every user
    if to_do == "bulk":
        total_calories = tdee_calc + 300
        protein = 2 * weight
        fats = total_calories / 36
        
    elif to_do == "mantain":
        total_calories = tdee_calc
        protein = 1.8 * weight
        fats = total_calories / 36
    
    elif to_do == "cut":
        total_calories = tdee_calc - 500
        protein = 2.5 * weight # You need a lot more of protein while cutting
        fats = total_calories / 45

    carbs = (total_calories - protein * 4 - fats * 9) / 4 # Formula get thanks to AI

    return total_calories, protein, fats, carbs


# That's an important thing for having the result of the variables
gender, age, weight, height = variables()
bmr_calc = bmr(gender, age, weight, height)
tdee_calc = tdee(bmr_calc)
bmi_calc, to_do = bmi(height, weight)
total_calories, protein, fats, carbs = macros(tdee_calc, weight, to_do)


# Then we print the calorie results for the user
print(f"--- YOUR PHYSICAL CHARACTERISTICS ---")
print(f"Your BMR is {bmr_calc:.0f} calories")
print(f"Your TDEE is {tdee_calc:.0f} calories")
print(f"Your BMI is {bmi_calc:.1f}\n")

print(f"--- YOUR MACROS ({to_do.upper()}) ---") # Upper gives the text in CAPITAL LETTER
print(f"Total calories: {total_calories:.0f} kcal")
print(f"Protein: {protein:.0f} g")
print(f"Fats: {fats:.0f} g")
print(f"Carbs: {carbs:.0f} g") # We don't want decimals anywhere in those