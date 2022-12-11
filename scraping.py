from bs4 import BeautifulSoup
from time import sleep
from pessoa import Produto, Departamento
import requests

def get_produtos(departamento, produtos):
    sleep(3)
    url = departamento.link
    page = requests.get(url)
    soup = BeautifulSoup(page.content,'html.parser')
    li = soup.find_all('ol', class_="items_container")[0].find_all('li')
    
    i = 0
    for produto in li:
        if i > 1:
            break
        i += 1
        price = ''
        name = produto.find('p').text
        price = produto.find('span',class_=('andes-money-amount__fraction')).text
        try:
            price += ','+ produto.find('span',class_=('andes-money-amount__cents andes-money-amount__cents--superscript-24')).text
        except:
            price +=',0'
        
        price = str(price)    
        price = price.replace('.','')
        price = price.replace(',','.')
        price = float(price)
        
        produtos.append(Produto(departamento, price, name))
    return produtos

def get_data():
    sleep(1)
    url = "https://www.mercadolivre.com.br/ofertas#nav-header"
    page = requests.get(url)
    soup = BeautifulSoup(page.content,'html.parser')
    aside = soup.find_all('aside')
    ols = aside[0].find_all('ol')
    a_tags = ols[1].find_all('a', href=True)
    departamentos = []
    links= []
    for link in a_tags:
        href = link.get('href')
        text = link.text.strip('0123456789() ')
        departamentos.append(Departamento(text, href))

    produtos = []

    for departamento in departamentos:
        get_produtos(departamento, produtos)
        print(departamento.nome)
    return produtos