from scraping import get_data
from database import *
 
products = get_data()

for product in products:
    insert_product(product)