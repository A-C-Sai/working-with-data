import requests
from bs4 import BeautifulSoup as bs
import re
import os
import shutil
import mysql.connector as sql



def obtainConnection(connector,h,u,pwd):
    connection = sql.connect(
        host = h,
        user = u,
        password = pwd
    )

    return connection


def initilize_database_table(cursor,query):
        create_data_base_query = f"CREATE DATABASE {query}"
        use_data_base_query = f"USE {query}"
        create_table_query = f"CREATE TABLE products (prod_name VARCHAR(2000), prod_price FLOAT, prod_rating FLOAT, img_path VARCHAR(200))"
    
        cursor.execute(f"DROP DATABASE IF EXISTS {query}")
        cursor.execute(create_data_base_query)
        cursor.execute(use_data_base_query)
        cursor.execute(create_table_query)


def clear_images(folder_path):
    try:
        # Walk through all the directories in the given path
        for root, dirs, files in os.walk(folder_path, topdown=False):
            for dir_name in dirs:
                dir_path = os.path.join(root, dir_name)
                shutil.rmtree(dir_path)
                print(f'Deleted folder: {dir_path}')
        print('All folders deleted successfully.')
    except Exception as e:
        print(f'Error: {e}')


def extractProductInfo(products,current_pg,headers,cursor,query):
    
    product_details = []

    for prod_num,product in enumerate(products):
        try:
            prod_name = (product.find("div",attrs={'data-cy':'title-recipe'})
                         .find("h2")
                         .find("a")
                         .find("span").text)
            prod_name = prod_name.replace('"',r'\"')
        except:
            continue

        try:
            prod_price = (product.find("div",attrs={'data-cy':'price-recipe'})
                          .find("span",attrs={'class':'a-price'})
                          .find("span",attrs={'class':'a-offscreen'})
                          .text)
            prod_price = float(prod_price.split("$")[1].replace(",",""))
        except:
            continue

        try:
            prod_rating = (product.find("span",attrs={'aria-label':re.compile(r'out of')})
                           .find("span",attrs={'class':'a-icon-alt'})
                           .text)
            prod_rating = float(prod_rating.split()[0])
        except:
            continue

        try:
            img_link = product.find("img",attrs={'class':'s-image'})['src']
            prod_img = requests.get(img_link,headers=headers).content
            img_path = f"static/images/{query}/{current_pg}/{prod_num}.jpg"
        except:
            continue

        try:
            with open(img_path,"wb") as f:
                f.write(prod_img)
        except Exception as e:
            print(e)
            continue
        
        product_details.append(
            {'prod_name':prod_name,
             'prod_price':prod_price,
             'prod_rating':prod_rating,
             'img_path':img_path
             }
            )

    return product_details
    
        


def storeDB(prod_name,prod_price,prod_rating,img_path,cursor,query):
    insert_query = f'INSERT INTO products VALUES ("{prod_name}",{prod_price},{prod_rating},"{img_path}")'

    try:
        cursor.execute(f"USE {query}")
        cursor.execute(insert_query)
    except sql.DatabaseError as e:
        print(insert_query)
        print(e)


def fetchData(cursor,search_query):

    images_folder_path = f'./static/images/{search_query}'
    clear_images(images_folder_path)
    initilize_database_table(cursor,search_query.replace(" ","_") )
    
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'}
    base_URL = 'https://www.amazon.com.au'
    URL_extension = f'/s?k={search_query.replace("_","+")}'
    
    all_products_details = {}

    while URL_extension:
        r = requests.get(base_URL+URL_extension,headers=headers)
        soup = bs(r.content,features="html.parser")
        content = soup.find("div",attrs={'class':'s-main-slot'})
        products = content.find_all("div",attrs={'data-asin':re.compile(r'\w+'),'data-index':re.compile(r'\d+')})

        current_page_number = content.find("span",attrs={'aria-label':re.compile(r'Current page')}).text
       
        os.makedirs(f"./static/images/{search_query}/{current_page_number}")
        
       
        products_per_page = extractProductInfo(products,current_page_number,headers,cursor,search_query)
        all_products_details[f'Page {current_page_number}'] = products_per_page

        try:
            next_page_link = content.find("a",attrs={'aria-label':re.compile(r'Go to next page')})['href']
        except TypeError:
            next_page_link = ""
            
        URL_extension = next_page_link

    for products in all_products_details.values():
        for product in products:
            storeDB(query=search_query.replace(" ","_"),cursor=cursor,**product)
    
    print('HANDING CONTROL BACK TO APP')


    
