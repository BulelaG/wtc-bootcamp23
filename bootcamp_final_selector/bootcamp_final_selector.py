def user_name():

    username = input("Enter username:")
    
    '''
    Use this function to get the user input (username)
    '''
    
    return username


def read_file(username):
    '''
    Use this function to open and read the contents of the file student_results.txt 
    in order that you may extract the users results
    '''
    file = "/home/bootcamp/Documents/WTC-Bootcamp2023/bootcamp_final_selector/student_results.txt"
    with open(file, "r") as f:
        f1=f.read()
        results = f1.split()
        student_results = []
    for t,x in enumerate(results):
        if x == username:
            student_results.append(results[t+2])
    print(student_results)
    return student_results

    # file="/home/wtc/Documents/Bulela_Gomoshe _Python101/Bootcamp_Helper_Resources-20220721T064717Z-001/Bootcamp_Helper_Resources/student_results.txt"
    # with open(file,"r") as f:
    #   f1=f.read()
    # results =f1.split()
    # student_results = []
    # for t,x in enumerate(results):
    #  if x== username:
    #     student_results.append(results[t+2])
    # print(student_results)

    # return student_results

    

    
def get_student_scores(student_results):


    list_scores = student_results

    
    '''
    Use this function to get all the users relevant scores
    '''
    
    return list_scores


def exam_score(list_scores):


    '''
    Use this function to calculate the users exam score:
    One for the exam (out of 100), 
    one for the group project (out of 10), 
    one for daily exercises (out of 30). 
    The exam will weigh 60%, the group project 20% and the daily exercises 20%.
-
    '''
    exam_score = (int(list_scores[0])/ 100) * 60
    print(exam_score)
    return round(exam_score)


def exam_percentage(list_scores):
    '''
    Use this function to calculate the users exam percentage:
    One for the exam (out of 100), 
    one for the group project (out of 10), 
    one for daily exercises (out of 30). 
    The exam will weigh 60%, the group project 20% and the daily exercises 20%.
    '''
    exam_percentage = (int(list_scores[0])/ 100) * 60

    print(exam_percentage)
    return round(exam_percentage)


def group_project_score(list_scores):

    '''
    Use this function to calculate the users group project score:
    One for the exam (out of 100), 
    one for the group project (out of 10), 
    one for daily exercises (out of 30). 
    The exam will weigh 60%, the group project 20% and the daily exercises 20%.
    '''
    group_project_score = (int(list_scores[1])/ 10) * 20

    print(group_project_score)
    return round(group_project_score)


def group_project_percentage(list_scores):
    '''
    Use this function to calculate the users group project percentage:
    One for the exam (out of 100), 
    one for the group project (out of 10), 
    one for daily exercises (out of 30). 
    The exam will weigh 60%, the group project 20% and the daily exercises 20%.
    '''
    group_project_percentage = (int(list_scores[1])/ 10) * 20
    print(group_project_percentage)
    return round(group_project_percentage)
 

def daily_exercise_score(list_scores):
    '''
    Use this function to calculate the users daily exercise score:
    One for the exam (out of 100), 
    one for the group project (out of 10), 
    one for daily exercises (out of 30). 
    The exam will weigh 60%, the group project 20% and the daily exercises 20%.
    '''
    daily_exercise_score = (int(list_scores[1])/ 30) * 20

    print(daily_exercise_score)
    return round(daily_exercise_score)


def daily_exercise_percentage(list_scores):
    '''
    Use this function to calculate the users daily exercise percentage:
    One for the exam (out of 100), 
    one for the group project (out of 10), 
    one for daily exercises (out of 30). 
    The exam will weigh 60%, the group project 20% and the daily exercises 20%.
    '''
    daily_exercise_percentage = (int(list_scores[1])/ 30) * 20
    print(daily_exercise_percentage)
    return round(daily_exercise_percentage)


def final_result(exam_result, group_project, daily_exercise):
    '''
    Use this function to calculate the user's final result out a 100
    '''
    final_result = ((exam_result / 100) * 60) + group_project + ((daily_exercise / 30) * 20)
    print(final_result)
    return round(final_result)


def type_of_pass(final_result):
    '''
    Use this function to determine whether they scored a first class pass, or an average pass 
    or if the user has failed.
    '''
    if final_result in range(90,101):
        type_of_pass = ("first class pass")
    elif final_result in range(30,81):
     type_of_pass = (" pass")
    else : 
     type_of_pass = ("fail")
     print(type_of_pass)
    return type_of_pass



if __name__ == '__main__':
    '''
    Do not edit this section, these are the function calls
    '''
    username = user_name()
    student_results = read_file(username)
    list_scores = get_student_scores(student_results)
    exam_result = exam_score(list_scores)
    exam_percentage = exam_percentage(list_scores)
    group_project = group_project_score(list_scores)
    group_project_percentage = group_project_percentage(list_scores)
    daily_exercise = daily_exercise_score(list_scores)
    daily_exercise_percentage = daily_exercise_percentage(list_scores)
    average_score = final_result(exam_result, group_project, daily_exercise)
    type_of_pass(average_score)