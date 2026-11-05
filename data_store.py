def main():
    #Least Effective: Singular Storage
    name = "Tim"
    age = 26
    major = "Computer Science"
    gpa = 3.87

    #More Effective: N-Tuple
    student_one = ("Tim",26,"Computer Science",3.87)

    #Even More Effective: Disctionary
    student_one = {'name' : "Tim",
                   'age' : 26,
                   'major' : "Computer Science",
                   'gpa' : 3.87}

    students = {'student_one' : ("Tim",26,"Computer Science",3.87)}

    students2 = {'student_one' : 
                    {'name' : "Tim",
                   'age' : 26,
                   'major' : "Computer Science",
                   'gpa' : 3.87}}

    print(f"test")

if __name__ == "__main__":
    main()