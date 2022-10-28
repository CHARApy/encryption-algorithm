class txtdo:
    def __init__(self):
        self.pattern = {'0': 'sodgui ', '1': 'auhiko ', '2': 'aiogag ', '3': 'wphoui ', '4': 'paghus ',
                        '5': 'aioegb ', '6': 'aogphu ', '7': 'gheiau ', '8': 'tuoirp ', '9': 'qghuio '}
        self.re_pattern = ['sodgui', 'auhiko', 'aiogag', 'wphoui',
                           'paghus', 'aioegb', 'aogphu', 'gheiau', 'tuoirp', 'qghuio']

    def save(self, name):
        with open(name, 'w', encoding='utf-8') as f:  # 打开文件
            f.write(self.output)  # 写入文件

    def load(self, name):
        with open(name, 'r', encoding='utf-8') as f:  # 读取
            self.message = f.read()  # 存储在变量


class Code(txtdo):
    def __init__(self):
        super().__init__()
        self.message = ''
        self.key = 0

    def get_input(self):
        self.message = input('message: ')
        self.key = int(input('key: '))

    def load(self, name='add.txt'):
        txtdo.load(self, name)

    def to_ord_add_key(self):
        self.output = ''
        for x in self.message:
            value = ord(x) + self.key
            x = chr(value)
            self.output += x

    def to_list(self):
        self.output_2 = ''
        for x in self.output:
            x = ord(x)
            self.output_2 += str(x)+'|'
        list_str = list(self.output_2)
        list_str.pop()
        self.list_str = list_str

    def rep_lst_str(self):
        rep = [self.pattern[x] if x in self.pattern else x for x in self.list_str]
        output = ''.join(rep)
        self.output = output
        print('加密后：', self.output)

    def save(self, name='scr.txt'):
        txtdo.save(self, name)

    def run(self, if_load=False, if_save=False, loadplace=None, saveplace=None, key=None, message=None):
        if message != None and key != None:
            self.message = message
            self.key = key
            self.to_ord_add_key()
            self.to_list()
            self.rep_lst_str()
        else:
            if if_load:
                if loadplace == None:
                    self.load()
                else:
                    self.load(loadplace)
            else:
                self.get_input()
            self.to_ord_add_key()
            self.to_list()
            self.rep_lst_str()
        if if_save:
            if saveplace == None:
                self.save()
            else:
                self.save(saveplace)
        
        return self.output


class DeCode(txtdo):
    def __init__(self):
        super().__init__()

    def load(self, name='scr.txt'):
        if self.key == None:
            self.key = int(input('key: '))
        txtdo.load(self, name)

    def get_input(self):
        self.message = input('massage: ')
        if not self.key == None:
            self.key = input('key: ')

    def str_rep(self):
        message = ''
        for i in range(len(self.re_pattern)):
            self.message = self.message.replace(self.re_pattern[i], str(i))

        for y in self.message:
            if not y == ' ':
                message = message + y
        self.message = message

    def to_chr_add_key(self):
        lml = self.message.split('|')
        output = ''
        for x in lml:
            x = int(x)
            x -= self.key
            value = chr(x)
            output += value
        self.output = output
        print('解密后的信息：', output)

    def save(self, name='add.txt'):
        txtdo.save(self, name)

    def run(self, if_load=False, if_save=False, key=None, loadplace=None, saveplace=None, message=None):
        if message != None and key != None:
            self.message = message
            self.key = key
            self.str_rep()
            self.to_chr_add_key()
        else:
            self.key = key
            if if_load:
                if loadplace == None:
                    self.load()
                else:
                    self.load(loadplace)
            else:
                self.get_input()
            self.str_rep()
            self.to_chr_add_key()
        if if_save:
            if saveplace == None:
                self.save()
            else:
                self.save(saveplace)

        return self.output


if __name__ == '__main__':
    wenben = Code()
    wenben.run(if_load=True, if_save=True,
               loadplace='add.txt', saveplace='scr.txt')
    wenben.run(message='abc', key=0, if_save=True)

    mima = DeCode()
    mima.run(if_load=True, if_save=True, key=0,
             loadplace='scr.txt', saveplace='add.txt')
    mima.run(message='wphoui paghus |wphoui auhiko |wphoui auhiko |aioegb |wphoui gheiau |wphoui tuoirp |wphoui qghuio', key=0, if_save=True)
