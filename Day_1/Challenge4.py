#Temperature Converter

def to_Celsius(n):
    return (n-32)*5/9
def to_farenheat(n):
    return n*(9/5)+32

n=float(int(input("Enter temperature")))
choice=int(input("Enter your choise: 1.to celsious, 2. to farenheat"))
if choice == 1:
    print(n,"=",to_Celsius(n)) 
elif choice == 2:
    print(n,"=",to_farenheat(n))
else:
    print("Invalid choise")