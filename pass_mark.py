class_score = int(input('\n Enter Any Size of Class You Want: ')) 

pass_student = 0
fail_student = 0
sum = 0
for score in range(class_score):
    pass_mark = int(input("\n Enter Marks (0 - 100): "))
    
    if pass_mark < 0 or pass_mark > 100:
        print('Invalid Marks!!!')
        break
    elif pass_mark >= 45:
        pass_student = pass_student + 1
        sum += pass_mark
    else: # 0 <= mark < 50
        fail_student = fail_student + 1
        sum += pass_mark

print('\n The Total Student That Passed: ', pass_student)
print('\n The Total Student That Failed: ', fail_student)
print('\n The Average Grade Of All Student is: ', sum // (pass_student + fail_student))