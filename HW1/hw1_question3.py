#homework_org_1.3, Book-keeping


subj1_all_students= {'Taly':[55,46],
        'Guy':[70,60],
        'Omer':[80,70],
        'Michal':[90,99]}

subj2_all_students= {'Orly':[70,84],
        'Guy':[70,80],
        'Omer':[70,45],
        'Michal':[100,40]}



def compare_subjects_within_student(subj1_all_students,
                                    subj2_all_students):
    """
    Compare the two subjects with their students and print out the "preferred"
    subject for each student. Single-subject students shouldn't be printed.

    Choice for the data structure of the function's arguments is up to you.
    """
        #solution
    best={}

    #high grade within the subject:
    for key in subj1_all_students:
        subj1_all_students[key].remove(min(subj1_all_students[key]))

    for key in subj2_all_students:
        subj2_all_students[key].remove(min(subj2_all_students[key]))


    #best subject:
    #sub1
    for key in subj1_all_students:
        if key in subj2_all_students:
                if subj1_all_students[key]<=subj2_all_students[key]:
                    #print(key, 'subj2', subj2_all_students[key])
                    best[key]=['subj2', subj2_all_students[key]]
                else:
                # print(key,'subj1', subj1_all_students[key])
                    best[key]=['subj1', subj1_all_students[key]]
        #else:
            #print(key, 'subj1', subj1_all_students[key])
        #   best[key]=['subj1', subj1_all_students[key]]

    #sub2
    #for key in subj2_all_students:
    #  if key in subj1_all_students:
    #         pass
        #else:
            #print(key, 'subj2', subj2_all_students[key])
        #   best[key]=['subj2', subj2_all_students[key]]
    return best



if __name__ == '__main__':
    #Question 3
    subj1_all_students= {'Taly':[55,46],
        'Guy':[70,60],
        'Omer':[80,70],
        'Michal':[90,99]}

    subj2_all_students= {'Orly':[70,84],
        'Guy':[70,80],
        'Omer':[70,45],
        'Michal':[100,40]}


    return_value = compare_subjects_within_student(subj1_all_students,
                                    subj2_all_students)
    print('Question 1 example input: ',subj1_all_students, subj2_all_students)
    print(f"Question 1 solution: {return_value}")
