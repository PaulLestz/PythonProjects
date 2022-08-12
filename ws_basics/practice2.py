from bs4 import BeautifulSoup
import re

with open('ws_basics/index2.html', 'r') as html_file:
    doc = BeautifulSoup(html_file, 'lxml')

    tag = doc.find('option')
    tag['color'] = 'blue'
    print(tag['value']) #course-type
    print(tag) # shows that we can add attributes (e.g. color)
    print(tag.attrs) # dictionary of attributes to type

    # ---------------------------
    print('---------------------', end = '\n\n')

    tags = doc.find_all(['p', 'option']) # can search for multiple tags

    print(tags)

    undergrad_option = doc.find('option', text = "Undergraduate") # can filter

    print(undergrad_option)

    failed_undergraduate_option = doc.find('option', text = "Undergraduate", value = 'undergrad')

    print(failed_undergraduate_option) # None

    # ---------------------------
    print('---------------------', end = '\n\n')

    # REGULAR EXPRESSIONS

    re_tags = doc.find_all(text = re.compile("\$.*"), limit = 1) # CAN SET LIMITS ON RESULTS SHOWN
    print([tag.strip() for tag in re_tags])

    # ---------------------------
    print('---------------------', end = '\n\n')

    text_tags = doc.find_all('input', type = 'text')
    for tag in text_tags:
        tag['placeholder'] = 'I changed you!'
    
    with open('changed.html', 'w') as file:
        file.write(str(doc))


    print(doc.find('alpha'))