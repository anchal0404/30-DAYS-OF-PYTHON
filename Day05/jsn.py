import json


fp = open('Anchal.txt','a')
name = input("Account holder name? ")
account= int(input("Account no.: "))
Amount=int(input("Amount you wanna deposite"))

dict = {'name': name, 'account': account, 'amount':Amount}
json.dump(dict,fp)
fp.seek(0)
print(fp.read())