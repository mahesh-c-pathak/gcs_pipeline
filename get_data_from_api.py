import requests
import json
import pandas as pd
import time
import csv
import os

from datetime import datetime

def get_data():
    url = "https://randomuser.me/api/"
    res = requests.get(url)
    res = res.json()
    res = res['results'][0]
    return res

def format_data(res):
    data={}
    data['first_name'] = res['name']['first']
    data['last_name'] = res['name']['last']
    # data['dob'] = datetime.strptime(res['dob']['date'], '%Y-%m-%dT%H:%M:%S.%fZ')
    data['dob'] = res['dob']['date']
    data['gender'] = res['gender']
    data['postcode'] = res['location']['postcode']
    return data


def data_to_csv(dict):
    data_list = [dict]
    path = 'Name.csv'
    # create file with header if not exists
    if not os.path.exists(path):
        field_names = ['first_name', 'last_name', 'dob', 'gender', 'postcode']
        with open('Name.csv' , 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=field_names)
            writer.writeheader()
    # append data        
    field_names = ['first_name', 'last_name', 'dob', 'gender', 'postcode']
    with open('Name.csv', 'a', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=field_names)
                writer.writerows(data_list)

def data_to_pandas(dict):
    df = pd.DataFrame(dict, index=['i',])
    df.dob = pd.to_datetime(df.dob )
    return df



if __name__== "__main__":

    df = pd.DataFrame()

    curr_time = time.time()

    while 1==1:
        if time.time() > curr_time + 60:
            break
        try:
            res = get_data()
            res = format_data(res)   
            data_to_csv(res)
            df1 = data_to_pandas(res)
            df = df._append(df1,ignore_index=True)
            time.sleep(4)      
        except exception as e:
            logging.error(f"An error occured: {e}")
            continue

    print(df)
    

# to send to kafka serialise data
    # json.dumps(res).encode('utf8')

# formated data to csv

# formated data to pandas dataframe
    # columns=['first_name', 'last_name', 'dob', 'gender']
    # datetime_object = datetime.strptime(datetime_str, '%m/%d/%y %H:%M:%S')
    
    


