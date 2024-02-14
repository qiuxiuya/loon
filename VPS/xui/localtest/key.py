import sys
import requests
import re
keyword = input("请输入关键词: ")

url = f"https://bgp.he.net/search?search%5Bsearch={keyword}&commit=SearchS"
response = requests.get(url)

if response.status_code == 200:
    ipcird_list = re.findall(r'\b\d+\.\d+\.\d+\.\d+/\d+\b', response.text)
    ipcird_list = list(set(ipcird_list))
    with open("ipcird.txt", "w") as file:
        for ipcird in ipcird_list:
            file.write(ipcird + "\n")
    print("Done")
else:
    print("Failed")
