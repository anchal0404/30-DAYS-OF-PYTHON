DataBase= {
            1:{},
            2:{},
            3:{},
            4:{},
            5:{},
            6:{},
            7:{},
            8:{},
            9:{},
            10:{} }
for i in range(1,11):
    print("Student name.\n")
    student_name=input("Enter the name of student:\n")
    DSD=int(input("enter the DSD_marks:"))
    CS=int(input("enter the CS_marks:"))
    OOP=int(input("enter the OOP_marks:"))

    DataBase[i]["student_name"]=student_name
    DataBase[i]["DSD"]=DSD
    DataBase[i]["CS"]=CS
    DataBase[i]["OOP"]=OOP

for j in range(1,11):
    print(DataBase[j])