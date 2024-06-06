#!/bin/bash
YELLOW='\033[1;33m'
RESET='\033[0m'

rm -rf /root/ssl
mkdir -p /root/ssl

openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /root/ssl/bing.key -out /root/ssl/bing.crt -subj "/C=US/ST=YourState/L=YourCity/O=YourOrganization/CN=www.bing.com" > /dev/null 2>&1
echo -e "${YELLOW}已生成bing自签证书\n证书公钥在: /root/ssl/bing.crt \n证书私钥在: /root/ssl/bing.key${RESET}"
