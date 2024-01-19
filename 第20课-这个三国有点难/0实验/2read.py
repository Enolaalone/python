# 打开原始文件（以二进制模式打开）
with open('小超市商品.txt', 'rb') as file:
    byte_data = file.read()

# 解码（将字节数据解码为字符串）
# 这里假设原始编码是GBK，这常用于中文Windows环境
str_data = byte_data.decode('gbk')

# 以UTF-8编码重新编码并保存到新文件
with open('小超市商品.txt', 'w', encoding='utf-8') as file:
    file.write(str_data)