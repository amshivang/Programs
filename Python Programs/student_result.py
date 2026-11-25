def evaluate_result(**kwargs):
    if not kwargs:
        return None

    total_marks = sum(kwargs.values())
    percentage = (total_marks / (len(kwargs) * 100)) * 100
    highest_subject = max(kwargs, key=kwargs.get)
    all_passed = all(mark >= 40 for mark in kwargs.values())
    result_status = 'Pass' if all_passed else 'Fail'
    return {
        'total_marks': total_marks,
        'percentage': percentage,
        'highest_subject': highest_subject,
        'highest_marks': kwargs[highest_subject],
        'status': result_status,
    }


def student_result(**kwargs):
    result = evaluate_result(**kwargs)
    if not result:
        return None

    print(f"Total Marks: {result['total_marks']:.2f}")
    print(f"Percentage: {result['percentage']:.2f}%")
    print(
        f"Highest Scoring Subject: {result['highest_subject']} "
        f"({result['highest_marks']:.2f})"
    )
    print(f"Result: {result['status']}")
    return result


if __name__ == '__main__':
    num_subjects = int(input('Enter number of subjects: '))
    subject_marks = {}
    for i in range(1, num_subjects + 1):
        sub_name = input(f'Enter subject {i} name: ').strip()
        marks = float(input(f'Enter marks for {sub_name}: '))
        subject_marks[sub_name] = marks

    student_result(**subject_marks)
