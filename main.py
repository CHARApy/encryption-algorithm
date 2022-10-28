import time 

keys = ['sodgui', 'auhiko', 'aiogag', 'wphoui', 'paghus', 'aioegb', 'aogphu', 'gheiau', 'tuoirp', 'qghuio'] # 设置加密keys，只能用同一程序解密
load_from_txt = False # 读取文件判断变量
add_from_txt = False
    
def add(): #加密函数
    if add_from_txt:
        if input('是否在程序同一文件夹下添加add.txt，文本文档内的内容为加密内容(y/n)：') == 'y':
            with open('add.txt', 'r', encoding='utf-8') as f:  # 读取
                message = f.read()  # 存储在变量
    else:
        message = input('输入要加密的信息：')  # 获取信息
    key = input('输入加密匙（数字形式，一般不超过2000）：') # 获取密钥
    key = int(key) # 转换密钥为整数形式
    output = ''
    # 将信息结合密钥进行第一次加密
    try:
        for x in message:
            value = ord(x) + key
            x = chr(value)
            output += x
    except:
        print('出现错误，您的密钥超出范围')
        return

    output_2 = ''
    # 信息分割
    for x in output:
        x = ord(x)
        output_2 += str(x)+'|'
    # 转换列表
    list_str = list(output_2)
    list_str.pop()
    output_2 = ''.join(list_str)
    # 第二次加密
    for i in range(len(keys)):
        output_2 = output_2.replace(str(i), keys[i]+' ')
    print('加密后为：', output_2) # 输出结果
    # 寻问问是否保存
    choose = input('是否保存加密内容在同一文件夹下scr.txt(不保存密钥)，请输入(y/n)：')
    # 保存
    if choose == 'y':
        with open('scr.txt', 'w', encoding='utf-8') as f: # 打开文件
            f.write(output_2) # 写入文件
        print('成功！')
    # 不保存
    else:
        print('保存取消！')
    

def load(): #解密函数
    lml = []
    message_2 = ''
    # 判断是否从文件读取
    if load_from_txt:
        try:
            with open('scr.txt', 'r', encoding='utf-8') as f: # 读取
                message = f.read() #存储在变量
            print('读取成功')
        except:
            print('找不到文件或文件格式有误')
    # 若没有读取则询问信息
    else:
        print('信息之间用|分开')
        message = input('输入要解密的信息：')
    # 第一层解密
    for i in range(len(keys)):
        message = message.replace(keys[i], str(i))
    # 转换解密内容
    for y in message:
        if not y == ' ':
            message_2 = message_2 + y
    # 询问密钥
    key = input('输入加密时使用的秘钥：') 
    key = int(key)
    output = ''
    lml = message_2.split('|') # 切分列表
    #第二层解密
    try:
        for x in lml:
            x = int(x)
            x = x - key
            value = chr(x)
            output += value
    except:
        print('出现错误，您的密钥超出范围')
        return
    # 输出
    print('解密后的信息：', output)

    # 寻问问是否保存
    choose = input('是否保存加密内容在同一文件夹下add.txt(不保存密钥)，请输入(y/n)：')
    # 保存
    if choose == 'y':
        with open('add.txt', 'w', encoding='utf-8') as f:  # 打开文件
            f.write(output)  # 写入文件
        print('成功！')
    # 不保存
    else:
        print('保存取消！')

print('=欢迎使用=')
print('版本信息：加密器v2.1 Beta')
print('制作人：Chara')
# 程序运行
while True:
    print('########################################################')
    command = input('1.加密, 2.解密, 3.从文件加密, 4.从文件解密, 5.退出:')
    if command == '1':
        try:
            add()# 调用加密
        except:
            print('出现错误，请重试')
    elif command == '2':
        try:
            load()# 调用解密
        except:
            print('出现错误，请重试')
    elif command == '3':
        try:
            add_from_txt = True
            add()
            add_from_txt = False
        except:
            print('出现错误，请重试')
            add_from_txt = False
    elif command == '4':
        try:
            load_from_txt = True # 设置可以从文件读取
            load()
            load_from_txt = False
        except:
            print('出现错误，请重试')
            load_from_txt = False
    elif command == '5':
        print('谢谢使用')
        time.sleep(2)
        break # 退出
    else:
        print('选择有误，请重新选择') # 报错
