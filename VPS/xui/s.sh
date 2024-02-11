cvv(){
    python3 s.py
}

echo "Reading IP addresses from ipcird.txt..."
while IFS= read -r sbip || [[ -n "$sbip" ]]; do
    echo "Scanning IP: $sbip"
    masscan -p54321 "$sbip" --max-rate 1000 -oG results.txt
    cvv
done < ipcird.txt

echo "Scanning completed."
