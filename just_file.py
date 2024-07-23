import requests
import bs4
from fake_headers import Headers
import json

parsed_data = []

def fake_headers():
    return Headers(browser="chrome", os="win").generate()

response = requests.get('https://spb.hh.ru/search/vacancy?text=python&area=1&area=2',
                        headers=fake_headers())
main_page_data = bs4.BeautifulSoup(response.text,
                                   features='lxml')
articles = main_page_data.find_all('div', class_="vacancy-serp-item")

for article in articles:
    a_tag = article.find('a', class_="bloko-link")
    link = a_tag['href']
    salary_fork = article.find('span', class_="fake-magritte-primary-text--Hdw8FvkOzzOcoR4xXWni compensation-text--kTJ0_rp54B2vNeZ3CTt2 separate-line-on-xs--mtby5gO4J0ixtqzW38wh")
    company_name = article.find('span', class_="company-info-text--vgvZouLtf8jwBmaD1xgp").text
    city_name = article.find('span', class_="fake-magritte-primary-text--Hdw8FvkOzzOcoR4xXWni").text.split('\n')[-1].strip()
    description = article.find('div', class_='vacancy-serp-item__text').text
    if "Django" in description and "Flask" in description:
        parsed_data.append({
            'link': link,
            'salary': salary_fork.text if salary_fork else 'Не указана',
            'company_name': company_name,
            'city_name': city_name,
        })

with open('articles.json', 'w') as f:
    f.write(json.dumps(parsed_data, ensure_ascii=False, indent=4))