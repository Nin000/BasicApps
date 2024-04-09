from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://escueladirecta-blog.blogspot.com').text

sopa = BeautifulSoup(source, 'lxml')

csv_file = open('scrap_result.csv', 'w')

csv_writer = csv.writer(csv_file)

csv_writer.writerow(['titulo', 'autor', 'link'])

for article in sopa.find_all('article', class_='post-outer-container'):

    titulo = article.find('h3', class_='post-title entry-title').find('div', class_='r-snippetized').text
    print(titulo)

    autor = article.find("a", class_="g-profile").text
    print(autor)

    link = article.find('h3', class_='post-title entry-title').a['href']
    print(link)

    print()

    csv_writer.writerow([titulo.strip() , autor.strip() , link.strip()])

csv_file.close()
