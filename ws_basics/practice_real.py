from bs4 import BeautifulSoup
import requests
import time

print('Put some skill that you are not familiar with (separate multiple by spaces):')
unfamiliar_skills = input('>').split()
print(f'Filtering out: {unfamiliar_skills}')

def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text

    soup = BeautifulSoup(html_text, 'lxml')

    jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')

    for index, job in enumerate(jobs):
        published_date = job.find('span', class_ = 'sim-posted').span.text

        if 'few' not in published_date:
            continue

        company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ','')
        skills = job.find('span', class_ = 'srp-skills').text.replace(' ','')
        more_info = job.header.h2.a['href']

        break_out = False

        for unfamiliar_skill in unfamiliar_skills:
            if unfamiliar_skill in skills:
                break_out = True

        if break_out:
            continue

        with open(f'ws_basics/posts/{index}.txt', 'w') as f:
            f.write(f'Company Name: {company_name.strip()}\n')
            f.write(f'Required Skills: {skills.strip()}\n')
            f.write(f'More Info: {more_info}\n')
        print(f'File saved: {index}')

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'Waiting {time_wait} minutes...')
        time.sleep(3)