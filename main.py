from markbook import create_assignment, create_classroom, calculate_average_mark, add_student_to_classroom, edit_student, remove_student_from_classroom
import json
prompt =  ('\n----WELCOME TO YOUR MARKBOOK----\n\n' + '1. Create a new assingment.\n'
    +'2. Add a new class.\n' +'3. Calculate average mark.\n' + '4. Add student to classroom.\n'
    +'5. Remove student from classroom.\n'+'6. Edit a student.\n' +'0. Exit.\n'
    +'\nPlease enter the number that coressponds with what you would like to do: ')

def clear_screen():
    print('\n' *100)
def copy():
    with open("markbook.json", 'r') as f:
        copy = json.loads(f.read())
    
    return copy
def overwrite(text):
    with open('markbook.json', 'w') as f:
        text = json.dumps(text, indent=4)
        f.write(text)
def class_search(copy):
    classrooms = copy['classrooms']
    # prints all the classroom codes
    for idx, value in enumerate(classrooms):
        course_codes = value.get('course_code')
        print('\n', str(idx+1) + '.', course_codes)
    #gets classroom index
    classroom = int(input('\n0. Go back \n\n' 
    + 'Which classroom are you searching for?: '))
    classroom -= 1 
    
    if classroom == -1:
        return None
    # returns classroom dict
    return classrooms[classroom]
def student_search(classroom):
    #getting student list from classroom
    student_list = classroom['student_list']
    # if its empty
    if student_list == []:
        print('There are no students yet')
        return None
    # printing the students
    for idx, value in enumerate(student_list):
        f_names = value.get('first_name')
        l_names = value.get('last_name')
        print('\n', str(idx) + '.', f_names, l_names,)
    #grabbing the student index
    student = int(input('\n'+'Which student are you looking for?: '))
    #returns student dictionary
    return student_list[student] 

while True:
    while True:
        try:
            page = int(input(prompt))
            break
        except ValueError: 
            print('\nPlease input an integer that coressponds to your choice')
    
    if page == 0: # exit
        break
        
    elif page == 1: # add assignment
        clear_screen()
        print('---ADDING AN ASSIGNMNET---')
        # collecting inputs
        name = input("Please Input the name of the assignment or '0' to go back: ")
        if name == '0':
            clear_screen()
            continue
        due = input('Input the due date: ')
        points = int(input('Input the points: '))
        # making the assignment
        assignment = (create_assignment(name, due, points))
        copy = copy()
        # getting classroom for assignment
        classroom = class_search(copy)
        
        if classroom == None:
            break
        # appending to assignments list
        assignment_list = classroom["assignment_list"]
        assignment_list.append(assignment)
        print("Just created an assignment with the following details:\n\n", assignment)
        print("Here are all the assignments\n\n", assignment_list)
        overwrite(copy)

        page = int(input(prompt))
    
    elif page == 2: # create a classroom
        clear_screen()
        print('---CREATING A CLASSROOM---')
        while True:
            try:
                # collecting inputs
                course_code = input("Please Input the name of the assignment or '0' to go back: ")
                if course_code == '0':
                    break
                course_name = input('course_name: ')
                period = int(input('period: '))
                teacher = input('teacher: ')
                break
            
            except ValueError:
                print('Please input an integer for the period')
        #make the classroom
        classroom = create_classroom(course_name, course_name, period, teacher)
        copy = copy()
        # append classroom to the classrooms list
        classrooms = copy["classrooms"]
        classrooms.append(classroom)
        
        overwrite(copy)
        print("Just created a classroom with the following details:")
        print(classrooms[-1])

        page = int(input(prompt))
    
    elif page == 3: # calculate student average
        clear_screen()
        print('---CALCULATE STUDENT AVERAGE---')
        copy = copy()
        classroom = class_search(copy)

        if classroom == None:
            break
        
        student = student_search(classroom)

        average = calculate_average_mark(student)
        
        print(student.get('first_name'), student.get('last_name'), 'Average:', average, '%')

        page = int(input(prompt))
    
    elif page == 4: # add student
        clear_screen()
        print('---ADD A STUDENT---')
        copy = copy()
        classroom = class_search(copy)

        if classroom == None:
            break
        
        # collecting inputs
        student_fname = input("The student's first name: ")
        student_lname = input("The student's last name: ")
        grade = int(input("The student's grade: "))
        student_number = int(input("The student's student number: "))
        gender = input("The student's gender: ")
        email = input("The student's email: ")
        
        # collect marks
        marks = input("The student's marks sperated by comma + space, ex. '100, 95, 90': ")
        marks = marks.split(', ')
        
        # marks to int list
        for i in range(0, len (marks)):
            marks[i] = int(marks[i])
        
        # comments to str list
        comments = input("student's comments  sperated by comma + space, ex. 'hi, yellow, red': ")
        comments = comments.split(', ')
        
        #student info to dict
        student = {"first_name":student_fname, "last_name":student_lname, 
        "grade": grade, "student_number": student_number, "gender":gender, "email":email, "marks": marks, "comments":comments}
        
        #printing new student list 
        print(add_student_to_classroom(student, classroom))
        overwrite(copy)
        
        page = int(input(prompt))
    
    elif page == 5: #remove student
        clear_screen()
        print('---REMOVE A STUDENT---')
        copy = copy()
        classroom = class_search(copy)

        if classroom == None:
            break 
        
        #getting student
        student = student_search(classroom)
        print(student)
        print('0 = False, 1 = True')
        
        #confriming student
        confirm = int(input('Are you sure that you want to remove', student.get('first_name'), student.get('last_name'), 'from', classroom.get('Course_name')))
        
        #removing student
        if confirm:
            remove_student_from_classroom(student, classroom)
        
        else:
            break
        page = int(input(prompt))

    elif page == 6: #edit a student WIP
        clear_screen()
        print('---EDIT A STUDENT (WIP)---')
        copy = copy()
        classroom = class_search(copy)
        if classroom == None:
            break 
        
        student = student_search(classroom)

        kwargs = input()
        
        edit_student(student, kwargs)
        
        page = int(input(prompt))

    else:
        print('\nPlease input an integer that coressponds to your choice')
        page = int(input(prompt))
