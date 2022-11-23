# Task: Add to existing code a midlife crisis age group with $0 price tag
# Age range 45-55 

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

# Logics
# Height 120 or higher? Y-check age N-decline
# Age under 12? Y-$5 N-check next age group
# Age 18 or under? Y-$7 N-$12 (for adults and since midlife age group is free)
# Add photo? Y-$3

if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
  if age < 12:
    bill += 5
    print("Child tickets are $5.")
  elif age <= 18:
    bill += 7
    print("Youth tickets are $7.")
  elif age >= 45 and age <= 55:
    bill += 0
    print("Everything is going to be ok. Have a free ride on us!")
  else:
    bill += 12
    print("Adult tickets are $12.")
  
  wants_photo = input("Do you want a photo taken? Y or N. ")
  if wants_photo == "Y":
    bill += 3
  
  print(f"Your final bill is ${bill}")

else:
  print("Sorry, you have to grow taller before you can ride.")
