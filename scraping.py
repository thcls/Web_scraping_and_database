from bs4 import BeautifulSoup
from time import sleep
from product import *
from requests import get
from csv import writer

def get_products(departament, products):
    url = departament.link
    sleep(2)
    page = get(url)
    soup = BeautifulSoup(page.content,'html.parser')
    li = soup.find_all('ol', class_="items_container")[0].find_all('li')
    
    for product in li:
        price = ''
        name = product.find('p').text
        price = product.find('span',class_=('andes-money-amount__fraction')).text
        
        try:
            price += ','+ product.find('span',class_=('andes-money-amount__cents andes-money-amount__cents--superscript-24')).text
        except:
            price +=',0'
        
        price = str(price)    
        price = price.replace('.','')
        price = price.replace(',','.')
        price = float(price)
        
        products.append(Product(departament, price, name))
        
    return products

def get_csv(products):
    with open('products.csv', 'w') as file:
        csvwriter = writer(file)
        csvwriter.writerow(['Name','Price','Departament name'])
        for product in products:
            csvwriter.writerow([product.name, str(product.price), product.departament.name])

def get_data():
    url = "https://www.mercadolivre.com.br/ofertas#nav-header"
    page = get(url)
    
    soup = BeautifulSoup(page.content,'html.parser')
    aside = soup.find_all('aside')
    ols = aside[0].find_all('ol')
    a_tags = ols[1].find_all('a', href=True)
    
    departaments = []
    links= []
    
    for link in a_tags:
        href = link.get('href')
        text = link.text.strip('0123456789() ')
        departaments.append(Department(text, href))

    products = []

    print('Scraping departaments...\n')
    
    for departament in departaments:
        get_products(departament, products)
        departament.show()
    
    get_csv(products)
    
    return products, departaments

