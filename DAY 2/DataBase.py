print("WELCOME TO THE DATABASE")
student_name=[]
ED_marks=[]
DSD_marks=[]
EMI_marks=[]
AC_marks=[]
CS_marks=[]
Civil_marks=[]
Total=[]
sum = 0
for i in range(1,11):
 name=input("Enter the name of {}th student: \n".format(i))
 student_name.append(name)
 ed=int(input("Enter the marks in ED"))
 ED_marks.append(ed)
 dsd=int(input("Enter the marks in DSD "))
 DSD_marks.append(dsd)
 emi=int(input("Enter the marks in EMI"))
 EMI_marks.append(emi)
 ac=int(input("Enter the marks in AC"))
 AC_marks.append(ac)
 cs=int(input("Enter the marks in CS"))
 CS_marks.append(cs)
 civil=int(input("Enter the marks in CIVIL"))
 Civil_marks.append(civil)
 sum= ed + dsd + emi + ac + cs + civil
Choose=int(input("whose marks wanna see?"))
j=6*(Choose-1)






