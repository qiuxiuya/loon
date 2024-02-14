rm ipcird.txt
echo "请选择模式："
echo "1. ASN"
echo "2. Keyword"
read mode

if [ $mode -eq 1 ]; then
    python3 asn.py
elif [ $mode -eq 2 ]; then
    python3 key.py
else
    echo "输入错误，请重新执行脚本。"
    exit 1
fi
