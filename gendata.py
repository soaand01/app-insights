import requests
import time

for data in range(15):
    data1 = requests.get('http://127.0.0.1:8080')
    time.sleep(2)
    data2 = requests.get('http://127.0.0.1:8080/error')
    print(data1.text)
    print(data2.text)