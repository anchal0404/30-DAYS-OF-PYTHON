
fp = open("Anchal.txt", "a")
u=input("What is your name?")
h=input("What is your profession?")
k=input("What is your hobby?")
t=input("Why Should we hire you?")
y=input("Your contact no.:")
fp.write("What is your name? \n")
fp.write("u")
fp.write(" \n What is your profession? \n  ")
fp.write(h)
fp.write("\n What is your hobby? \n ")
fp.write(k)
fp.write("\n Why Should we hire you? \n ")
fp.write(t)
fp.write("\n Your contact no. \n ")
fp.write(y)
fp.seek(0)
print(fp.read())