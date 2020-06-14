start = 0xA1A1
end = 0xFEFE
for code in range(start, end):
    hex_str = '%x' % code
    bytes_obj = bytes.fromhex(hex_str)
    try:
        print(str(bytes_obj, 'gb2312'))
        with open("./gb2312.txt", "a", encoding="utf-8") as f:
            f.write(str(bytes_obj, 'gb2312')+"\n")
    except Exception as e:
        pass