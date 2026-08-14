def student_result(**kwargs):
    if not kwargs:
        return
        
    total_marks = sum(kwargs.values())
    percentage = (total_marks / (len(kwargs) * 100)) * 100
    highest_subject = max(kwargs, key=kwargs.get)
    all_passed = all(mark >= 40 for mark in kwargs.values())
    result_status = 'Pass' if all_passed else 'Fail'
    
    print(f'Total Marks: {total_marks:.2f}')
    print(f'Percentage: {percentage:.2f}%')
    print(f'Highest Scoring Subject: {highest_subject} ({kwargs[highest_subject]:.2f})')
    print(f'Result: {result_status}')

num_subjects = int(input('Enter number of subjects: '))
subject_marks = {}
for i in range(1, num_subjects + 1):
    sub_name = input(f'Enter subject {i} name: ').strip()
    marks = float(input(f'Enter marks for {sub_name}: '))
    subject_marks[sub_name] = marks

student_result(**subject_marks)
