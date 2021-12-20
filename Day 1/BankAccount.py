print('Welcome to Dena Bank')
balance=10000
exist=input('Do You have any account YES and NO?')
if exist == "YES":
    X = int(input('Enter you Account Number'))
else:
    print("Please Create new account")


print('Do you want to Credit or Deposit?')
u=input('enter C for credit and D for deposit \n')
if (u =='C'):
    print('enter the amount you wanna credit:')
    f=int(input('enter the amount'))
    amount=balance+f
    print(amount)

elif (u=='D'):
    print('enter the amount you wanna deposit:')
    f=int(input('enter the amount'))
    amount=balance-f
    print(amount)
else:
    print("thankyou")
   

   






