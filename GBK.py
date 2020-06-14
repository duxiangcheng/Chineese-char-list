start = 0x8140
end = 0xFEFE
i = 0
for code in range(start, end):
    hex_str = '%x' % code
    bytes_obj = bytes.fromhex(hex_str)
    try:
        print(str(bytes_obj, 'gbk'))
        with open("./keys_gbk.txt", "a", encoding="utf-8") as f:
            f.write(str(bytes_obj, 'gbk'))
    except Exception as e:
        pass