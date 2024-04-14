import requests
import pandas as pd
import os

data = pd.read_excel("touringplans_data_dictionary.xlsx")
urls = data.iloc[:,0].to_list()

for url in urls:
    
    response = requests.get(url)

    if response.status_code == 200:
        print(f"Successfully downloaded {url}")
        os.makedirs("./dataset", exist_ok=True)
        path = f"./dataset/{os.path.basename(url)}"

        with open(path, 'wb') as f:
            f.write(response.content)
    
    else:
        print(f"Fail to download {url}")