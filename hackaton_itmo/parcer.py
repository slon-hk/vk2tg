from bs4 import BeautifulSoup
from lxml import etree
import requests
import random


company = []


def hh_ru(keyword, region=1):
    company = []
    def get_vacancies(keyword):
        url = "https://api.hh.ru/vacancies"
        params = {
            "text": keyword,
            "area": region,  #ID егиона
            "per_page": 100, #количество вакансий в поиске <=100
            "experience": "noExperience",#Опыт
            "employment": "probation" #Тип занятости
        }
        headers = {
            "User-Agent": "Your User Agent",  # Replace with your User-Agent header
        }

        response = requests.get(url, params=params, headers=headers)

        if response.status_code == 200:
            data = response.json()
            vacancies = data.get("items", [])
            s_s = 0
            s_r = 0
            for vacancy in vacancies:
                # Получение информации о компании
                vacancy_title = vacancy.get("name")#Название вакансии
                if len(vacancy_title) > 60:
                    vacancy_title = vacancy_title[:57] + "..."
                vacancy_url = vacancy.get("alternate_url")#Ссылка на объявление
                company_name = vacancy.get("employer", {}).get("name")#азвание компании
                company_salary = vacancy.get("salary")#ЗП


                
                #ЗП и добавление в массив
                if company_salary != None:
                    if company_salary["from"] != None and company_salary["to"] != None:
                        pass
                        company.append([vacancy_title, company_name, str(company_salary["from"])+" - "+str(company_salary["to"]), str(random.uniform(3, 5))[0:3] + "☆", vacancy_url])
                    elif company_salary["to"] != None and company_salary["from"] == None:
                        company.append([vacancy_title, company_name, "До "+str(company_salary["to"]), str(random.uniform(2, 5))[0:3] + "☆", vacancy_url])
                    elif company_salary["to"] == None and company_salary["from"] != None:
                        company.append([vacancy_title, company_name, "От "+str(company_salary["from"]), str(random.uniform(1, 5))[0:3] + "☆",vacancy_url])
                else:
                    company_salary = "Не указана"
                    company.append([vacancy_title, company_name, company_salary, str(random.uniform(3, 5))[0:3] + "☆",vacancy_url])
        else:
            print(f"Request failed with status code: {response.status_code}")

    # Example usage
    get_vacancies(keyword)
    s_s = sum(i[2] for i in company if i[2].isdigit())
    s_r = sum(float(i[3][:-1]) for i in company)

    avg_s = round(s_s / len(company), 3)
    avg_r = round(s_r / len(company), 3)

    company2 = []

    for i in company:
        a = i[2] / avg_s if i[2].isdigit() else 0
        a += float(i[3][:-1]) / avg_r

        company2.append([a] + i)

    print(company2)

    company2 = list(reversed(sorted(company2)))

    return company2


def uptome(keyword, region):
    url = f"https://career.habr.com/vacancies?q={keyword}&s[]=2&s[]=3&s[]=82&s[]=4&s[]=5&s[]=72&s[]=1&s[]=75&s[]=6&s[]=77&s[]=7&s[]=83&s[]=84&s[]=8&s[]=85&s[]=73&s[]=9&s[]=86&s[]=106&type=all"
    print(url)
    response = requests.get(url)
    bs = BeautifulSoup(response.text, 'html.parser')
    jobs_list = bs.find("div", class_="vacancy-card__info")
    name_job = jobs_list.find("a", class_="vacancy-card__title-link").text
    name_company = jobs_list.find("div", class_="vacancy-card__company").find("a", class_="link-comp link-comp--appearance-dark").text
    company_sallary = jobs_list.find("div", class_="vacancy-card__salary").find("div", class_="basic-salary").text
    company_rating = str(random.uniform(3, 5))[0:2]
    url_company = "https://career.habr.com/"+jobs_list.find("div", class_="vacancy-card__title").find("a").get("href")
    if company_sallary=="":
        company_sallary = None
    company.append([name_job, name_company, company_sallary, company_rating, url_company])