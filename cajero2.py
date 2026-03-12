initial_value=1000 

print ("Welcome to the ATM")
print (f"You have {initial_value} in your account")

withdraw= float(input("How much you want to withdraw?: "))


if withdraw > initial_value:
    print("Insufficient founds")

elif withdraw <=0:
    print("Invalid amount")
else:
    new_value= initial_value-withdraw
    print("Your withdraw have been succesfully")
    print(f"Now you have {new_value} dollars in your account  ")





    

