import requests
import json
import pandas as pd

response = requests.get('https://uat.fastag.ai/account/mockable_test/')

print(response.status_code)


try:
    # search_data = input("Enter The API key to be searched: ")

    data  = response.text

    data_json = json.loads(data)

    print(type(data_json))
    
    # print(data_json['search_data'])
    # key_data = dict(filter(lambda item : search_data in item[0], data_json.items()))

    # if data_json['search_data']:
    #     print("Data found")
    # else: 
    #     print("Data not found")

    # print("Key value pair of searched data : " + str(key_data))


    
except:
    print('An error has occured')