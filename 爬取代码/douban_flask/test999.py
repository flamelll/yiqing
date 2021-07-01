# 打开旧文件
f = open('D:/360MoveData/Users/ASUS/Desktop/大三上王建民/企业异常信息判断/zzsfp_hwmx.txt','r',encoding='utf-8')

# 打开新文件
f_new = open('D:/360MoveData/Users/ASUS/Desktop/大三上王建民/企业异常信息判断/zzsfp1_hwmx.txt','w',encoding='utf-8')


# 循环读取旧文件
for line in f:
    # 进行判断
    if "(" in line:
        line = line.replace('(fpid_','')
        line = line.replace(')','')
    # 如果不符合就正常的将文件中的内容读取并且输出到新文件中
    f_new.write(line)

f.close()
f_new.close()