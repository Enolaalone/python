CodeText_0=[]
CodeText_1=[]
set=input('按1加密     按2解密')
txt=input('输入密文')
if set=='1':
    behind=int(input('加密位数'))
    for i in txt:
        CodeText_0.append(ord(i))

    for i in CodeText_0:
        if 48<=i<=57:
            CodeText_1.append((i-48+behind)%10+48)
        elif 97<=i<=122:
            CodeText_1.append((i-97+behind)%26+97)
        elif 65<=i<=90:
            CodeText_1.append((i-65+behind)%26+65)
        else:
            CodeText_1.append(ord('*'))

    for i in CodeText_1:
        print(chr(i),end='')

else:
    behind = int(input('加密位数'))
    for i in txt:
        CodeText_0.append(ord(i))

    for i in CodeText_0:
        if 48 <= i <= 57:
            CodeText_1.append((i - 48 - behind) % 10 + 48)
        elif 97 <= i <= 122:
            CodeText_1.append((i - 97 - behind) % 26 + 97)
        elif 65 <= i <= 90:
            CodeText_1.append((i - 65 - behind) % 26 + 65)
        else:
            CodeText_1.append(ord('*'))

    for i in CodeText_1:
        print(chr(i), end='')



