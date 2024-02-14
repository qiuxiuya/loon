import sys
import requests
import re
as_number = input("请输入AS号: ")
url = f"https://bgp.he.net/AS{as_number}#_prefixes"
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
