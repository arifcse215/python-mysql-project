import mysql.connector

conn = mysql.connector.connect(
    user = "root",
    password = "1112",
    host = "localhost",
    port = 3306,
    database = "student"
)
cur = conn.cursor()

# Create table.
# cur.execute(
#     """
#     create table if not exists student_info(
#     id int auto_increment primary key,
#     name varchar(50),
#     age int check(age > 0),
#     city varchar(30)
#     )
#     """
# )

def add_student():
    sql = "insert into student_info(name, age, city) values(%s, %s, %s)"
    name = input("Name: ")
    try:
        age = int(input("Age: "))
    except:
        print("Wrong input. Age will be in Digit.")

    city = input("City: ")
    val = (name, age, city)
    print()

    try:
        cur.execute(sql, val)
        conn.commit()
        print("Add student successfully\n")
    except:
        print("Something went wrong!\n")
        conn.rollback()

def view_student():
    cur.execute("select * from student_info")
    print("-------------------------")
    for data in cur:
        print(f"\tID: {data[0]}")
        print(f"\tName: {data[1]}")
        print(f"\tAge: {data[2]}")
        print(f"\tCity: {data[3]}")
        print("-------------------------")
    print()

def searchById():
    stu_id = int(input("Enter ID: "))
    print()
    sql = "select * from student_info where id = %s"
    cur.execute(sql, (stu_id, ))
    print("-------------------------")
    for x in cur:
        print(f"Name: {x[1]}")
        print(f"Age: {x[2]}")
        print(f"City: {x[3]}")
    print("-------------------------")

    print()

def searchByName():
    stu_name = input("Enter Name: ")
    sql = "select * from student_info where name = %s"
    print()
    cur.execute(sql, (stu_name,))
    
    print("-------------------------")
    for x in cur:
        print(f"ID: {x[0]}")
        print(f"Name: {x[1]}")
        print(f"Age: {x[2]}")
        print(f"City: {x[3]}")
        print("-------------------------")

    print()

def update_data():
    print()
    print("1. Update Name")
    print("2. Update Age")
    print("3. Update City")
    print("0. Update Deny")

    num = int(input("Select Option: "))

    if num == 1:
        s_id = int(input("Student ID: "))
        new_name = input("New Name: ")

        sql = "update student_info set name = %s where id = %s"
        val = (new_name, s_id)

        try:
            cur.execute(sql, val)
            conn.commit()
            print("Update Successfull.")
        except Exception as e:
            print(e)
            conn.rollback()
    elif num == 2:
        s_id  = int(input("Student ID: "))
        new_age = int(input("New Age: "))

        sql = "update student_info set age = %s where id = %s"
        val = (new_age, s_id)

        try:
            cur.execute(sql, val)
            conn.commit()
            print("update Successfull.")
        except Exception as e:
            print(e)
            conn.rollback()
    elif num == 3:
        s_id = int(input("Student ID: "))
        new_city = input("New City: ")

        sql = "update student_info set city = %s where id =%s"
        val = (new_city, s_id)

        try:
            cur.execute(sql, val)
            conn.commit()
            print("Update Successfull.")
        except Exception as e:
            print(e)
            conn.rollback()
    elif num == 0:
        return 0
    

while True:
    print("Selec Option\n")
    print("\t1. Add Student")
    print("\t2. View All Students")
    print("\t3. Search by ID")
    print("\t4. Search by Name")
    print("\t5. Update Student")
    print("\t0 to Exit")
    print()
    try:
        number = int(input("Choise Option: "))
        print()
    except:
        number = int(input("Enter Digit: "))
        print()

    if number == 0:
        print("Bye Bye!")
        break
    elif number == 1:
        add_student()
    elif number == 2:
        view_student()
    elif number == 3:
        searchById()
    elif number == 4:
        searchByName()
    elif number == 5:
        update_data()
    else:
        print("Press correct number")
        print()
cur.close()
conn.close()