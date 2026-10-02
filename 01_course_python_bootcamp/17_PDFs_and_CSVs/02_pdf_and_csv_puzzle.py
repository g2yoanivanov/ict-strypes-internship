import csv
import pypdf
import re


def print_link_from_csv():
    data = open('find_the_link.csv', encoding='utf-8')

    csv_data = csv.reader(data)
    data_lines = list(csv_data)

    allowed = set("-._~:/?#[]@!$&'()*+,;=")
    link = []

    for line in data_lines:
        for cell in line:
            if cell.isalpha() or cell in allowed:
                link.append(cell)

    print(''.join(link))


def find_phone_in_pdf():
    file = open('Find_the_Phone_Number.pdf', 'rb')
    pdf = pypdf.PdfReader(file)

    pages = len(pdf.pages)

    pattern = r'\d{3}.\d{3}.\d{4}' 

    for n in range(pages):
    
        page  = pdf.pages[n]
        page_text = page.extract_text()
        match = re.search(pattern,page_text)
        
        if match:
            print(match.group())


print_link_from_csv()
find_phone_in_pdf()