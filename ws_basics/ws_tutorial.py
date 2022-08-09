from bs4 import BeautifulSoup

with open('index.html', 'r') as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content, 'lxml')

    print(soup.prettify()) # Prints HTML, but with proper indentation

    first_list_tag = soup.find('li') # bs4.element.Tag type
    list_tags = soup.find_all('li') # array of bs4.element.Tag types

    print(list_tags)

    for list_elem in list_tags:
        print(list_elem.text)

    # ---------------------------
    print('---------------------', end = '\n\n')

    blurb_div = soup.find('div', class_ = 'blurb')

    print(blurb_div.prettify())

    intro = ' '.join(blurb_div.h1.text.split()[-2:])
    question = blurb_div.p.text

    print(f'{intro}, {question}')

