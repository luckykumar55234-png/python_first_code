import requests
import json
import logging

logging.basicConfig(
    filename="app.log",
    filemode="a",
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)
try:
    logging.info("data fetch ho rha h")
    url = ("https://dummyjson.com/roducts/category/beauty")

    resphone = requests.get(url)
    data = resphone.json()
    logging.info("Success = Data successfully mil gya")

    print("Total products:",len(data)) 


except Exception as error:
    print("Except:",error)
    logging.error("Failed = data not found")




    























 