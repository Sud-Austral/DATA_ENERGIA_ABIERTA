import requests
import json
import pandas as pd
import sys
import codecs

#:

def proceso():
    url  = 'http://cne.cloudapi.junar.com/api/v2/datastreams/CAPAC-INSTA-DE-GENER-TOTAL/data.pjson/?auth_key=QIupCcn5gQC4U61tB1h8e5GjmrEAefVII90h6z7x&limit=5000'
    response = requests.get(url)
    decoded_data=codecs.decode(response.content, 'utf-8-sig')
    d = json.loads(decoded_data)
    df = pd.DataFrame(d["result"])
    df.to_excel("ELECTRICIDAD/CAPAC-INSTA-DE-GENER-TOTAL.xlsx", index=False)
    return df    

if __name__ == '__main__':    
    try:
        proceso()
    except:
        error = sys.exc_info()[1]
        print(error)
    
