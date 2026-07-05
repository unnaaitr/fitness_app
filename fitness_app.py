# FITNESS APP BUILT WITH PYTHON

# This app will be using Mifflin-St Jeor equation to calculate the Basal Metabolic Rate
# It's the most common formula used to estimate the number of calories burned at rest, based on some variables

def bmr():
    while True:
        gender = input("Please, enter your gender (male/female): ").strip().lower()

        if gender in ["male", "female"]:
            print(f"You're a {gender}\n")
            age = int(input("Please, enter your age: "))

            if age < 14 or age > 90:
                print("Age must be between 14 and 90")

            else:
                print(f"You're {age} years old\n")
                weight = float(input("Please, enter your weight in kg: "))

                if weight < 30 or weight > 300:
                    print("Weight must be between 30 and 300 kg")

                else:
                    print(f"You're weighted {weight} kg\n")
                    height = float(input("Please, enter you height in cm"))

                    if height < 70 or height > 250:
                        print("Height must be between 70 and 250 cm")
                    
                    else:
                        print(f"You're {height} cm tall\n")
                        break

        else:
            print("Choose between male or female")

    return(gender, age, weight, height)

bmr()