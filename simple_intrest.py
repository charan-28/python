print("Welcome to the Simple Interest and Compound Interest Calculator!")
print("Select an option:")
print("1. Calculate Simple Interest")
print("2. Calculate Compound Interest")
print("3. Calculate Amount")
print("4. Exit")

n=int(input("Select a number how we can help you: "))
if n>0 and n<=4:
    if n==1:
        p=int(input("Enter the principal amount: "))
        r=int(input("Enter the rate of interest: "))
        t=int(input("Enter the time in years: "))
        si=(p*r*t)/100
        print(f"Simple Interest: {si:.2f}")
    elif n==2:
        p=int(input("Enter the principal amount: "))
        r=int(input("Enter the rate of interest: "))
        t=int(input("Enter the time in years: "))
        ci=p*(1+r/100)**t-p
        print(f"Compound Interest: {ci:.2f}")
    elif n==3:
        p=int(input("Enter the principal amount: "))
        r=int(input("Enter the rate of interest: "))
        t=int(input("Enter the time in years: "))
        a=p*(1+r/100)**t
        print(f"Amount after {t} years: {a:.2f}")
    elif n==4:
        print("Thank you for using our services!")
    elif n>4:
        print("Invalid option selected. Please select a valid option.")
