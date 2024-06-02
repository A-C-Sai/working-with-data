from flask import Flask
from flask import render_template
from flask import request
import mysql.connector as sql
import scrape
import display
from dotenv import load_dotenv, find_dotenv
import os
load_dotenv(find_dotenv())


app = Flask(__name__)


@app.route('/',methods=['GET','POST'])
def home():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        connection_password = os.environ.get("MySQL_PWD")
        connection = scrape.obtainConnection(sql,'localhost','root',connection_password)
        cursor = connection.cursor()
        print('HANDING CONTROL TO scrape')
        scrape.fetchData(cursor, request.form['search'].strip())    
        connection.commit()
        all_products = display.retrieveData(request.form['search'].strip().replace(" ","_"),cursor)
        print('CLOSING CONNECTION')
        connection.close()
        return render_template('products.html',products=all_products)



if __name__ == '__main__':
    app.run(debug=True)