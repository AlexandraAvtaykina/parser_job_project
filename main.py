from utils import choice_1, choice_2


user_answer = int(input(f''' Где искать вакансии? \n1. HeadHunter\n2. SuperJob\n'''))

if user_answer == 1:
    choice_1()
elif user_answer == 2:
    choice_2()
else:
    print('Некорректный ввод')
