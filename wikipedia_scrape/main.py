from bs4 import BeautifulSoup
import requests
from WikipediaScrapeErrors import IncorrectInputError
import time as clock


base_url = 'https://en.wikipedia.org'

def collect_page_links(link: str) -> "list[str]":
    """Examines a wikipedia page and collects all unique links found in its 
    body paragraphs

    Arguments:
        link -- the URL for the wikipedia page whose links are being collected

    Returns:
        A list of all unique links from this page found in its body paragraphs

    Throws:
        IncorrectInputError if link is not a valid Wikipedia URL
    """

    link_urls: "set[str]" = set()

    html_text = requests.get(link).text
    doc = BeautifulSoup(html_text, 'lxml')
    body_text = doc.find('div', id = 'bodyContent').find('div', class_ = 'mw-parser-output')

    # Checks for invalid Wikipedia URL
    if body_text.find('table', id = 'noarticletext') != None:
        raise IncorrectInputError(f'{link} is not a valid Wikipedia URL')

    paragraph_texts = body_text.find_all('p')

    for paragraph in paragraph_texts:
        links = paragraph.find_all('a')

        for link in links:
            link_urls.add(base_url + link['href'])

    return list(filter(lambda link: link.startswith('https://en.wikipedia.org/wiki/'), link_urls))

def links_contain_end_title(links: "list[str]", desired_title: str) -> bool:
    for link in links:

        page_title: str = link.split('/')[-1].replace("_", " ")

        if page_title.lower() == desired_title.lower():
            return True
    
    return False



if __name__ == '__main__':
    starting_url = input("Enter starting URL: ")
    global_links = {starting_url: collect_page_links(starting_url)}
    desired_title = "Tidal acceleration"
    end_found = False

    starting_time = clock.time()
    while(not end_found):
        if links_contain_end_title(global_links, desired_title):
            print(desired_title + f' was found on {starting_url}')
            end_found = True
        else:
            temp_links = global_links.copy()
            global_links.clear()
            for link in temp_links.keys():
                global_links +=collect_page_links(link)
    ending_time = clock.time()
    total_seconds = ending_time - starting_time

    print(f'Time Elapsed: {total_seconds * 1000} ms')