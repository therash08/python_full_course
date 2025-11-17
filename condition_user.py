# age = int(input("enter a number: "))
# if age >= 18:
#     print("eligible")
# else:
#     print("no eligible")


# num = int(input("enter a number: "))
# if num > 0:
#     print("positive")
# else:
#     print("negetives")

# marks = int(input("enter your number: "))

# if marks >= 90:
#     print("Grade A+")
# elif marks >= 80:
#     print("Grade A")
# elif marks >= 70:
#     print("Grade A-")
# elif marks >= 60:
#     print("Grade B")
# elif marks >= 50:
#     print("Grade c")
# else:
#     print("Grade f")

# username = input("enter username: ")
# passowrd = input("enter pass: ")

# if username == "admin":
#     if passowrd == "12334":
#         print("logging hoise")
#     else:
#         print("incorrrect number")
# else:
#     print("unknown username")

# password = ""
# while password != "python 123":
#     password = input("enter the password: ")
    
# print("access granted!")

# while True:
#     try:
#         Number = int(input("enter Number:"))
#         break
#     except ValueError:
#         print("invalid number! try again")
    
# print("thank you! you entered:", Number)

# age = 10

# if age <= 12:
#     print("Travel for free.")
# else:
#     print("Pay for ticket.")

# marks = 45
# res = "Pass" if marks >= 40 else "Fail"

# print(f"Result: {res}")

# age = 12

# if age <= 12:
#     print("Child.")
# elif age <= 19:
#     print("Teenager.")
# elif age <= 35:
#     print("Young adult.")
# else:
#     print("Adult.")
    
age = 50
is_member = True

if age >= 60:
    if is_member:
        print("30% senior discount!")
    else:
        print("20% senior discount.")
else:
    print("Not eligible for a senior discount.")