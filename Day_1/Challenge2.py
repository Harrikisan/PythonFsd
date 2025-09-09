#Shopping Cart Calculater

price1=int(input("Enter price of product1: "))
price2=int(input("Enter price of product2: "))
price3=int(input("Enter price of product3: "))
sum=price1+price2+price3
discounted=0
discount=0
if sum>100:
    discount=10
    discounted=sum*(10/100)
print("Cart Total: ",sum)
print("Discount: ",discounted)
print("Final total: ",sum-discounted)