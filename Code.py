n=int(input("Enter the numbers of apple teacher got to divide among the students\t"))
minimum_student=int(input("Enter the minimum student strength\t"))
maximum_student=int(input("Enter the maximum student strength\t"))
if minimum_student==maximum_student:
    print(f"You have {minimum_student} numbers of student in your class")
    print(f"You got {n} numbers of apple")
    if n%minimum_student==0:
        print(f"{minimum_student} is a divisor of {n} number of student , So you can distribute the apple equally to all")
        var=n/minimum_student
        print(f"Give {var} numbers of apple to all the students to divide it equally")
    elif n%minimum_student!=0:
        print(f"{minimum_student} is not a divisor of {n} number of student , So you cannot distribute the apple equally to all")

else:
    for i in range(minimum_student,maximum_student+1):
        if n%i==0:
            print(f"{i} is the divisor of {n} number of student, so you can divide them equally")
        else:
            print(f"{i} is not the divisor of {n} number of student, so you can not divide them equally")
