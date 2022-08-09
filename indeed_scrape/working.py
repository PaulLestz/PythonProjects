from requests_html import HTMLSession
import csv

def get_data(s, url):
    r = s.get(url)
    return r.html.find('div.job_seen_beacon'), r.html.find('ul.pagination-list a[aria-label=Next]')

def parse_html(html):
    job = {
        'title': html.find('h2 > a')[0].text.strip().replace('\n',''),
        'link': 'https://uk.indeed.com/viewjob?jk=' + html.find('h2 > a')[0].attrs['data-jk'],
        'company_name': html.find('span.companyName')[0].text.strip().replace('\n',''),
        'snippet': html.find('div.job-snippet')[0].text.strip().replace('\n','')
    }

    try:
        job['salary'] = html.find('div.metadata.salary-snippet-container')[0].text.strip().replace('\n','')
    except IndexError as err:
        # print(err)
        job['salary'] = 'None Given'

    return job

def export(results):
    keys = results[0].keys()
    with open('results.csv', 'w') as f:
        dict_writer = csv.DictWriter(f, keys)
        dict_writer.writeheader()
        dict_writer.writerows(results)

def main():
    results = []
    session = HTMLSession()
    base_url = 'https://uk.indeed.com'
    url = base_url + '/jobs?q=python%20developer&l=bristol&vjk=5bbb46b2c2062d17'
    
    while True:
        jobs = get_data(session, url)

        for job in jobs[0]:
            results.append(parse_html(job))

        try:
            url = base_url + jobs[1][0].attrs['href']
            print(url)
        except IndexError as err:
            # print(err)
            break
    export(results)

if __name__ == '__main__':
    main()