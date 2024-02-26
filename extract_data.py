import csv
import json
from data import get_registerd_user
import time
import datetime
import os
import pandas as pd

if __name__ == "__main__":

    curr_time = time.time()

    # dt = datetime.datetime.fromtimestamp(curr_time).strftime("%Y-%m-%d %H:%M:%S")
    curr_date = datetime.datetime.fromtimestamp(curr_time).strftime("%Y-%m-%d")
    start_time = datetime.datetime.fromtimestamp(curr_time).strftime("%H:%M:%S")

    path = f"./{curr_date}"

    try:
        os.mkdir(path )
    except OSError as e:
        print("Directory exists")

    # csv file_name
    file_name = f"Names_{start_time}.csv"

    file_path= f"{path}/{file_name}"
    # file_path= f"./{curr_date}/Names_{start_time}.csv"



    field_names = ['name', 'address', 'created_at'] 
    with open(file_path , 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=field_names)
        writer.writeheader()

    while 1==1:
        if time.time() > curr_time + 60:
            break
        try:
            registered_user = get_registerd_user()
            print(registered_user)
            user_list = [registered_user]
            with open(file_path, 'a', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=field_names)
                writer.writerows(user_list)
            time.sleep(4)
        except exception as e:
            logging.error(f"An error occured: {e}")
            continue
    df = pd.read_csv(file_path)
    print(df)