class Student(object):
    student_num = 0
    def add_student(self, student_info):
        with open("student.txt", "a") as file:
            file.write(student_info+'\n')
        return "添加成功"

    def get_student_info(self, student_num):
        with open("student.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                if student_num == line[0:5]:
                    result = line
                    break
            else:
                result = "没有该学号信息"
        return result

    def get_all_students_info(self):
        with open("student.txt", "r") as file:
            line = file.read()
            if line != "":
                result = line
            else:
                result = "还没添加学生信息"
        return result

    def delete_student(self, student_num):
        if not self.is_student_exsit(student_num):
            return "该学号不存在"
        with open("student.txt", "r") as file:
            lines = file.readlines()
        with open("student.txt", "w") as file:
            for line in lines:
                if student_num == line[0:5]:
                    continue
                file.write(line)
        return "删除成功"

    def edit_student(self, student_num):
        if not self.is_student_exsit(student_num):
            return "学号不存在"
        name = input("请输入学生姓名：")
        gender = input("请输入学生性别：")
        phone = input("请输入学生手机号：")
        student_info = ",".join([student_num, name, gender, phone])
        with open("student.txt", "r") as file:
            lines = file.readlines()
        with open("student.txt", "w") as file:
            for line in lines:
                if student_num == line[0:5]:
                    file.write(student_info+'\n')
                else:
                    file.write(line)
        return "学生信息修改成功"


    def is_student_exsit(self, student_num):
        with open("student.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                if student_num == line[0:5]:
                    return True
            else:
                return False

    def create_student_num(self):
        if self.student_num == 0:
            try:
                with open("student.txt", "r") as file:
                    lines = file.readlines()
                    last_line = lines[-1]
                    if last_line:
                        self.student_num = int(last_line.split(",")[0]) + 1
                    else:
                        self.student_num = 10001
            except:
                self.student_num = 10001
        else:
            self.student_num += 10001
        return str(self.student_num)


def show_message():
    print("=================")
    print("学生管理系统 V1.0.0")
    print("1：添加学生")
    print("2：查询学生信息")
    print("3：查询所以学生信息")
    print("4：删除学生信息")
    print("5：修改学生信息")
    print("0：退出系统")


def main():
    student = Student()
    while True:
        show_message()
        number = int(input("请输入系统菜单对应的数字："))
        if number == 1:
            name = input("请输入学生姓名：")
            gender = input("请输入学生性别：")
            phone = input("请输入学生手机号：")
            student_num = create_student_num()
            student_info = ",".join([student_num, name, gender, phone])
            result = student.add_student(student_info)
            print(result)
        elif number == 2:
            student_num = input("请输入要查询的学生学号：")
            result = student.get_student_info(student_num)
            print(result)
        elif number == 3:
            result = student.get_all_students_info()
            print(result)
        elif number == 4:
            student_num = input("请输入要删除的学生学号：")
            result = student.delete_student(student_num)
            print(result)
        elif number == 5:
            student_num = input("请输入要修改的学生学号：")
            result = student.edit_student(student_num)
            print(result)
        elif number == 0:
            print("退出系统")
            break
        else:
            print("请重新输入")



if __name__ == "__main__":
    main()