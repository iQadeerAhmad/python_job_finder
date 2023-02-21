#!/usr/bin/env python3

import time

import requests
from bs4 import BeautifulSoup


def find_python_jobs():
    url = 'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation='
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_="clearfix job-bx wht-shd-bx")
    
    for index, job in enumerate(jobs):
        published_date = job.find('span', class_='sim-posted').span.text
        save_job_details(job,index,published_date)


def save_job_details(job,index,publish_date):
    company_name = job.find("h3", class_='joblist-comp-name').text.replace(" ", '')
    skills = job.find('span', class_='srp-skills').text.replace(" ", '')
    more_info = job.header.h2.a['href']
    with open(f'posts/{index}.txt','w') as f:

        f.write(f'JobPost publish date: {publish_date}\n\n')
        f.write(f"Company Name: {company_name.strip()}\n\n")
        f.write(f"Skills Required: {skills.strip()}\n\n")
        f.write(f"More Info: {more_info}\n")
        

    print(f"Job is saved in posts/{index}.txt file")

if __name__ == "__main__":
    print('Do you want to run this script continuously? [y/n]')
    reuse = input('>')

    if reuse == 'y':
        print("After how many minutes should it regenerate data? (Enter a number between 1-10)")
        regenerate_interval = int(input(">"))
        
        while True:
            find_python_jobs()
            print(f"Waiting for {regenerate_interval} minutes...")
            time.sleep(regenerate_interval * 60)
    else:
        find_python_jobs()
