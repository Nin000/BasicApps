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

    autor = article.find('span').text

    link = article.find('h3', class_='post-title entry-title').a['href']

    print(titulo, autor, link)

    print()

    csv_writer.writerow([titulo, autor, link])

csv_file.close()
