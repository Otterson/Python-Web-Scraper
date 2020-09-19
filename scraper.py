import requests
from bs4 import BeautifulSoup

URL = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=Australia'
page = requests.get(URL)    ##request and fetch html request for link

html = BeautifulSoup(page.content, 'html.parser') #correct formatting on html response content

results = html.find(id='ResultsContainer')  #search for return data, found in ResultsContainer

job_elems = results.find_all('section', class_='card-content')

for job_elem in job_elems:
    title_elem = job_elem.find('h2', class_='title')
    company_elem = job_elem.find('div', class_='company')
    location_elem = job_elem.find('div', class_='location')
    if None in (title_elem, company_elem, location_elem):
        continue
    print(title_elem.text.strip())
    print(company_elem.text.strip())
    print(location_elem.text.strip())
    print()
    
python_jobs = results.find_all('h2', string='Python Developer') #filter by for python dev
print(python_jobs)

python_jobs = results.find_all('h2', string=lambda text: 'python' in text.lower()) #provides more flexibility with capitalization

for p_job in python_jobs:    #parses list and extracts application links
    link = p_job.find('a')['href'] #pulls link url
    print(p_job.text.strip())
    print("Apply here: {link}\n")





