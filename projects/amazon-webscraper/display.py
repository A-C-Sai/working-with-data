def retrieveData(search_query,cursor):
    query = f'SELECT * FROM {search_query}.products'
    cursor.execute(query)
    all_products = cursor.fetchall()

    return all_products


    