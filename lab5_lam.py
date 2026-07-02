# Lam Ngu | Lab 5 | Intro to Python     

#ticket 1
ages = [17, 11, 25, 13, 9]
for age in ages:
    if age >= 13:
        print("Access granted") # 17,25,13 will have Access
    else:
        print("Too young") # 11, 9 will have "Too young"
# the variable age holds a single number for the list moving from the left

#ticket 2

keep_checking = "yes"
while keep_checking == "yes":
    age = (int(input("Enter an age: ")))
    if age >= 13:
        print(f"{age} - Access granted")
    else:
        print(f"{age} - Too young")
    keep_checking = input("Check another age? (yes/no): ") #if users type no the loop will not run at all
# a while loop is a right choice because you dont know how many times the user want to check their age


# ticket 3

while True:
    age = input("Enter something or type stop: ")
    if age == "stop":
        break #if you forgot the break the loop will never end

# ticket 4
def can_access(age): #instead of using the comparison in the loop, now it uses true and false returns the result back to the if statement
    if age >= 13:
        return True
    else:
        return False
for age in ages:
    if can_access(age):
        print(f"{age} - Access granted")
    else:
        print(f"{age}- Too young")
# easier to resuse

# Ticket 5
signups = [22, 10, 15, 8, 19, 13]
def signup_report(age_list):
    approved = 0 
    print("--- Streampass Signup Report ---")
    for number, age in enumerate(age_list, start=1):
        if can_access(age):
            print(f"Signup #{number} | Age {age} - Access granted")
            approved += 1
        else:
            print(f"Signup #{number} | Age {age} - Too young!")
        print(f"Approved: {approved}) out of {len(age_list)}")
signup_report(signups)

