from classes import HeadHunterAPI, SuperJobAPI, Vacancy, JSONSaver

hh_api = HeadHunterAPI()
superjob_api = SuperJobAPI()
json_saver = JSONSaver()


def choice_1():
    user_answer_keyword = input(' Ключевое слово\n')
    hh_vacancies = hh_api.get_vacancies(user_answer_keyword)
    json_saver.add_vacancy(hh_vacancies)

    user_answer_action = int(input(""" Выберите действие: \n1. Выборка по городу\n2. Выборка по зарплате от
3. Получить все найденные вакансии\n4. Получить топ N вакансий по зарплате\n"""))

    if user_answer_action == 1:
        user_answer_city = input('Введите город\n')
        vac = hh_api.sort_vacancies_city(user_answer_keyword, user_answer_city)
        for v in vac:
            for i in v:
                # if v[i]['salary'] is not None and v[i]['salary']['from'] is not None:
                vac = Vacancy(job_title=v['name'], job_url=v['alternate_url'], salary=v['salary']['from'],
                        area_name=v['area']['name'])
                return vac
        # vac = [v for v in vac if v['salary'] is not None and v['salary']['from'] is not None]
        # vac = [Vacancy(job_title=v['name'], job_url=v['alternate_url'], salary=v['salary']['from'], area_name=v['area']['name']) for v in vac]

        # [print(v) for v in vac]

    elif user_answer_action == 2:

        vac = [v for v in hh_vacancies if v.get('salary') is not None and v.get('salary').get('from') is not None]
        vac = [Vacancy(job_title=v['name'], job_url=v['alternate_url'], salary=v['salary']['from'], area_name=v['area']['name']) for v in vac]

        vac = sorted(vac, reverse=True)

        [print(v) for v in vac]

        # vac = hh_api.sort_vacancies(user_answer_vac)
        # vac = [Vacancy(job_title=v['name'], job_url=v['alternate_url'], salary=v['salary']['from'],
        #                area_name=v['area']['name']) for v in vac]
        #
        # [print(v) for v in vac]

        # vac = hh_api.get_vacancies(user_answer_vac)
        # vac = [v for v in vac if v.get('salary') is not None and v.get('salary').get('from') is not None]
        # vac = [Vacancy(job_title=v['name'], job_url=v['alternate_url'], salary=v['salary']['from'],
        #                area_name=v['area']['name']) for v in vac]
        # user_answer_city = input('Введите город\n')
        # vac = hh_api.sort_vacancies_city(user_answer_vac, user_answer_city)
        # vac = [Vacancy(job_title=v['name'], job_url=v['alternate_url'], salary=v['salary']['from'],
        #                area_name=v['area']['name']) for v in vac]
        #
        # [print(v) for v in vac]
    elif user_answer_action == 3:
        vac = [v for v in hh_vacancies if v.get('salary') is not None and v.get('salary').get('from') is not None]
        vac = [Vacancy(job_title=v['name'], job_url=v['alternate_url'], salary=v['salary']['from'],
                       area_name=v['area']['name']) for v in vac]

        [print(v) for v in vac]

    elif user_answer_action == 4:
        top_n = int(input('Введите N\n'))
        vac = [v for v in hh_vacancies if v.get('salary') is not None and v.get('salary').get('from') is not None]
        vac = [Vacancy(job_title=v['name'], job_url=v['alternate_url'], salary=v['salary']['from'],
                       area_name=v['area']['name']) for v in vac]
        vac = sorted(vac, reverse=True)

        [print(v) for v in vac[:top_n]]

    else:
        print('Некорректный ввод')


def choice_2():
    user_answer_keyword = input(' Ключевое слово\n')
    superjob_vacancies = superjob_api.get_vacancies(user_answer_keyword)
    json_saver.add_vacancy(superjob_vacancies)

    user_answer_action = int(input(""" Выберите действие: \n1. Выборка по городу\n2. Выборка по зарплате от
3. Получить все найденные вакансии\n4. Получить топ N вакансий по зарплате\n"""))

    if user_answer_action == 1:
        user_answer_city = input('Введите город\n')
        vac = superjob_api.sort_vacancies_city(user_answer_keyword, user_answer_city)
        print(vac)
        # vac = [Vacancy(job_title=v['profession'], job_url=v['link'], salary=v['payment_from'],
        #                area_name=v['town']['title']) for v in vac]
        #
        # [print(v) for v in vac]

    elif user_answer_action == 2:
        vac = [Vacancy(job_title=v['profession'], job_url=v['link'], salary=v['payment_from'],
                       area_name=v['town']['title']) for v in superjob_vacancies]

        vac = sorted(vac, reverse=True)
        [print(v) for v in vac]

    elif user_answer_action == 3:
        vac = [Vacancy(job_title=v['profession'], job_url=v['link'], salary=v['payment_from'],
                       area_name=v['town']['title']) for v in superjob_vacancies]

        [print(v) for v in vac]

    elif user_answer_action == 4:
        top_n = int(input('Введите N\n'))
        vac = [Vacancy(job_title=v['profession'], job_url=v['link'], salary=v['payment_from'],
                       area_name=v['town']['title']) for v in superjob_vacancies]
        vac = sorted(vac, reverse=True)

        [print(v) for v in vac[:top_n]]

    else:
        print('Некорректный ввод')
