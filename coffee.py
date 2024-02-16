input_filename = 'coffee_data.txt'
output_filename = 'coffee_data.csv'

with open(input_filename, 'r', encoding='utf-8') as infile, \
        open(output_filename, 'w', encoding='utf-8') as outfile:

    while True:
        try:
            line1 = next(infile).strip()
            line2 = next(infile).strip()
            line3 = next(infile).strip()
            # 可能存在的空白行
            next(infile)
        except StopIteration:
            break
        parts = line1.split(' $')
        地區名稱 = parts[0].strip()
        價格重量 = '$' + parts[1].strip()
        價格, 重量 = 價格重量.split(' / ')

        parts = line2.replace('，', ',').split(', ')
        if len(parts) >= 3:
            品種, 處理方式 = parts[1], parts[2]
        else:
            品種, 處理方式 = parts[0], ''

        風味描述 = line3

        outfile.write(f'"{地區名稱}","{品種}","{價格}","{重量}","{處理方式}", {風味描述}\n')
