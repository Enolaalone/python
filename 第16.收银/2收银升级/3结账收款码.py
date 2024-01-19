ma=input('请出示付款码')
if len(ma)!=18 or ma[0:2] not in ['10','12','11','13','14','15']:
    print('无效码')
else:
    print('付款成功')