import requests
import pandas as pd
import subprocess as cmd


testing_url = 'https://api.rootnet.in/covid19-in/stats/testing/raw'

r = requests.get(url=testing_url)
data = pd.DataFrame(r.json()['data'])

