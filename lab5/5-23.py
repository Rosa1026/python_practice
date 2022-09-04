def how_many_persons(person_lst):
    res = int(len(person_lst)/5)

    return res

def compute_average_age(person_lst):
    age = 0
    
    for i in range(int(len(person_lst)/5)):
        age += person_lst[1+5*i]

    return age/int(len(person_lst)/5)

def count_males_females(person_lst):
    male = 0
    female = 0

    for i in range(int(len(person_lst)/5)):
        sex_index = person_lst[2+5*i]

        if sex_index == 0:
            female += 1
        else:
            male += 1

    return male, female

def display_persons(person_lst):
    for i in range(int(len(person_lst)/5)):
        print(person_lst[5*i:5+5*i])
    
person1 = ['온달', 20, 1, 180.0, 100.0]
person2 = ['이사부', 25, 1, 170.0, 70.0]
person3 = ['평강', 22, 0, 169.0, 60.0]
person4 = ['혁거세', 40, 1, 150.0, 50.0]

person_lst = person1+person3+person4
n_persons = how_many_persons(person_lst)
print(str(n_persons) + '명의 정보가 담겨 있습니다.')

person_lst = person1+person2+person3+person4
average_age = compute_average_age(person_lst)
print('평균 나이는 '+ str(average_age)+ '세입니다.')

n_male, n_female = count_males_females(person_lst)
print('리스트에는 남자가',n_male,'명, 여자가',n_female,'명입니다.')

display_persons(person_lst)
