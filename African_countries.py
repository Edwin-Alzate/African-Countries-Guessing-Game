# This program is a guessing game of African Countries

def life_hearts(lives):

    return "♥"*lives
# print(chr(0x2665)*3)  or  print("♥")


countries = ["Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cabo Verde", "Cameroon", 
             "Central African Republic", "Chad", "Comoros", "Ivory Coast", "Djibouti", "Democratic Republic of the Congo", 
             "Egypt", "Equatorial Guinea", "Eritrea", "Eswatini", "Ethiopia", "Gabon", "Gambia", "Ghana", "Guinea", 
             "Guinea-Bissau", "Kenya", "Lesotho", "Liberia", "Libya", "Madagascar", "Malawi", "Mali", "Mauritania", 
             "Mauritius", "Morocco", "Mozambique", "Namibia", "Niger", "Nigeria", "Republic of the Congo", "Rwanda", 
             "Sao Tome & Principe", "Senegal", "Seychelles", "Sierra Leone", "Somalia", "South Africa", "South Sudan", 
             "Sudan", "Tanzania", "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe"] 

print("--------------------------")
print("|                        |")
print("|        Countries       |")
print("|           of           |")
print("|         Africa         |")
print("|                        |")
print("|      Guessing Game     |")
print("|                        |")
print("--------------------------")
print("")

score = 0

lives = 5

print("Let's start guessing.") 

while len(countries) > 0 and lives > 0:       

    print(f"\nNumber of countries to guess: {len(countries)}")

    print(f"Your score is: {score}")

    print(f"You have {life_hearts(lives)} left.")       

    country = input("Enter your guess: ").title()

    if country in countries:

        print(f"Well done! {country} is in Africa.")

        countries.remove(country)

        score += 1

    else:
        print(f"Nice try but no! {country} is not in Africa.")

        lives -= 1   

print(f"\nEnd of the game buddy, you have run out of lives. Your final score is: {score}")

