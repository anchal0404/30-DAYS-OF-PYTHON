amount = 0
Product={'Shirt':399,'Jeans':699,'Hoodie':999}
Discount= {'H&M2022': 0.20,'TT2022':0.30,'ROADSTER22': 0.35}
print('Welcome to End of reason Sale')
cart=input('please add the required product in cart to do so type a')
while (cart!="t"):
    if cart == 'a'or'S'or 'J' or 'H':
      cart=input("type S for Shirt,J for jeans,H for Hoodie,t for  Total amount:")
    if (cart=='S'): 
      amount =amount + Product['Shirt']
    
    elif(cart=='J'):
      amount =amount + Product['Jeans']
    
    elif(cart=='H'):
      amount =amount + Product['Hoodie']  

else:
    if cart !='t':
        print("Your Cart is Empty Please shop a product to proceed")

    print("Your total amount is {}".format(amount))
print('Please apply coupon code to get discount on your cart')

coupon=input("enter the code")
if coupon in Discount.keys():
    amount=amount- amount*Discount[coupon]
    print("Amount to be paid after discount is {}".format(amount))
else:
    print("Your total amount is{}".format(amount))


