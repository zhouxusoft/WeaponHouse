'''
武器仓库管理系统 :
    1.仓库登录
    2.密码修改
    3.装备的添加
    4.装备的删除
    5.装备的属性修改
    6.装备的查询 :
        6.1装备的名程查询
        6.2装备的职业筛选
    7.装备列表

装备信息 :
    1.名称  string
    2.职业 :
        1.战士/2.射手/3.法师/4.其他  int
    3.品质 :
        1.白-普通   int
        2.绿-精良
        3.蓝-稀有
        4.紫-史诗
        5.橙-传说
        6.红-绝世
    4.各类属性 :
        基础伤害  int
        攻击距离  int 单位：米
        攻击速度  int 次数/每秒
        暴击率  int 双倍伤害
        战力  计算公式：[(基础伤害 * 非暴击几率) + (暴击伤害 * 暴击率)] * 攻击速度 * sqrt(攻击距离)

额外的 :
    武器库总战力（统计功能）
    武器平均战力（统计功能）
'''
import math
import os

class Weapon:
    def __init__(self, info):
        self.name = info[0]         #武器名称
        self.career = info[1]       #武器职业
        self.quality = info[2]      #武器品质
        self.damage = info[3]       #武器伤害
        self.speed = info[4]        #武器攻速
        self.range = info[5]        #攻击距离
        self.crit = info[6]         #暴击几率
        self.power = info[7]        #综合战力
        match self.career:          #给武器相应的属性赋予对应的值
            case 1:
                self.Tcareer = "战士"
            case 2:
                self.Tcareer = "射手"
            case 3:
                self.Tcareer = "法师"
            case _:
                self.Tcareer = "不详"
        match self.quality:
            case 1:
                self.Tquality = "普通"
            case 2:
                self.Tquality = "精良"
            case 3:
                self.Tquality = "稀有"
            case 4:
                self.Tquality = "史诗"
            case 5:
                self.Tquality = "传说"
            case 6:
                self.Tquality = "绝世"
            case _:
                self.Tquality = "不详"
    #output方法作用为输出武器信息
    def output(self):
        print("\t\t|     " + self.Tquality + " " + self.name + "  \t|")
        print("\t\t|     " + self.Tcareer + "  \t\t|")
        print("\t\t|     战斗力: " + str(int(self.power)) + "\t|")
        print("\t\t|     伤害: " + str(self.damage) + "\t\t|")
        print("\t\t|     速度: " + str(self.speed) + "\t\t|")
        print("\t\t|     距离: " + str(self.range) + "\t\t|")
        print("\t\t|     暴击: " + str(self.crit) + "\t\t|")

class House:
    def __init__(self):
        os.system("cls")  #运行前清屏
        self.login()
    def login(self):  #登入模块
        f = open("password.txt", "r+")
        self.password = f.read()
        if self.password == "":    #判断password文件是否为空，若为空则创建密码
            self.firstlogin(f)
        f.close()   #文件用完及时关闭
        print("=================欢迎使用武器仓库管理系统=================")
        print("\n\t----------- 请先输入管理员密码 ------------")
        print("\t\t     - 输入off退出 -")
        print("\n\t\t     >>>  ", end="")
        temp_password = input()  #记录用户输入的密码
        if temp_password == "off" or temp_password == "off":
            return
        elif temp_password == self.password:
            os.system("cls")    #运行完清屏
            print("\t\t      >>>登录成功<<<")
            self.house()   #登陆成功 进入下一个环节 仓库具体功能模块
        else:
            os.system("cls")
            print("\t\t  >>>您输入的密码有误<<<")
            self.login()   #密码输入错误重新输入
    def firstlogin(self,f):  #首次使用（password文件中密码为空）创建管理员密码
        print("=================欢迎使用武器仓库管理系统=================")
        print("\n\t-------- 首次使用需创建管理员密码 ---------")
        print("\t\t       - 输入密码 -")
        print("\n\t\t     >>>  ", end="")
        temp_password = input()
        f.write(temp_password)
        self.password = temp_password
        os.system("cls")  #运行后清屏
    def house(self):   #仓库具体功能模块
        print("=================欢迎使用武器仓库管理系统=================")
        print("\t--------------   一号仓库   --------------")
        print("\t\t +\t\t        +")
        print("\t\t |     <1> 新增武器     |")
        print("\t\t |     <2> 删除武器     |")
        print("\t\t |     <3> 修改武器     |")
        print("\t\t |     <4> 查找武器     |")
        print("\t\t |     <5> 武器列表     |")
        print("\t\t |     <9> 修改密码     |")
        print("\t\t |     <0> 退出         |")
        print("\t\t +\t\t        +")
        print("\n\t\t     >>>  ", end="")
        num = input()  #记录用户操作数
        #str.isdigit()用于判断string是否能转换为int，避免用户输入错误时程序报错终止
        if not num.isdigit():
            os.system("cls")
            print("\t\t    >>>您的输入有误<<<")
            self.house()   
        #python中，每个case是独立的逻辑，不需要使用break
        else:
            num = int(num)
            match num:
                case 1:
                    os.system("cls")
                    self.addWeapon()
                case 2:
                    os.system("cls")
                    self.addWeapon()
                case 3:
                    os.system("cls")
                    self.addWeapon()
                case 4:
                    os.system("cls")
                    self.addWeapon()
                case 5:
                    os.system("cls")
                    self.addWeapon()
                case 9:
                    os.system("cls")
                    self.addWeapon()
                case 0:
                    os.system("cls")
                    self.house()
                case _:
                    os.system("cls")
                    print("\t\t    >>>您的输入有误<<<")
                    self.house()
            
        
    def addWeapon(self):
        #初始化武器信息的八个参数
        weapon = ["", "", "", "", "", "", "", ""];
        #est用于判断以下输入操作是否合法，若不合法，通过while循环来重新输入
        #武器名输入
        est = 1;
        while est:
            #默认下一次不会再进入循环
            est = 0;
            #界面
            print("=================欢迎使用武器仓库管理系统=================")
            print("\n\t--------------   添加武器   --------------")
            print("\n\t              请输入武器名称")
            print("\t             - 输入off返回 -")
            print("\n\t\t     >>>  ", end="")
            weapon[0] = input();
            # 判断用户是否想返回
            if weapon[0] == "off" or weapon[0] == "OFF":
                return;
            # 判断用户输入数据长度是否合法，应在2-4个汉字之内
            if  weapon[0].__len__() > 4 or weapon[0].__len__() < 2:
                #修改判断条件，重新进入循环
                est = 1
                #清屏重新显示
                os.system("cls")
                #提示输入错误
                print("\t\t >>>武器名称过长或过短<<<")
                #直接进入下一次循环
                continue
            else:
                #注意以utf-8的形式打开带有中文的文件，否则会乱码
                f = open("weapon.txt", "r+" , encoding="utf-8")
                #将文件指针指向文件末尾
                f.seek(0, 2)
                #通过指向文件末尾，来获得文件的长度
                end = f.tell()
                #将为文件指针重新指向开头
                f.seek(0, 0)
                #list1用于存储文件中所有武器的信息
                list1 = []
                #通过循环按行读取文件信息
                while 1:
                    password = f.readline()
                    #将读取的信息进行处理，把每个信息放入列表中的对应位置
                    list1.append(password.split(" ")[0:])
                    #判断文件是否读到了末尾，并结束循环
                    if f.tell() >= end:
                        break
                #文件用完及时关闭
                f.close()
                for i in range(0,len(list1)):
                    if list1[i][0] == weapon[0]:
                        #修改判断条件，重新进入循环
                        est = 1
                        #清屏重新显示
                        os.system("cls")
                        #提示输入错误
                        print("\t\t >>>该名称的武器已存在<<<")
                #直接进入下一次循环
                #此continue语句要放在上面for语句的外面，否则跳出的时内层for循环而不是外层的while
                if est == 1:
                    continue
                #用户输入的数据合法，清屏进入下一步操作
                os.system("cls")
        #武器职业输入
        est = 1
        while est:
            #默认下一次不会再进入循环
            est = 0;
            #界面
            print("=================欢迎使用武器仓库管理系统=================")
            print("\n\t--------------   添加武器   --------------")
            print("\n\t              请输入武器职业")
            print("\n\t\t        <1> 战士")
            print("\t\t        <2> 射手")
            print("\t\t        <3> 法师")
            print("\t\t        <4> 不详")
            print("\n\t\t     >>>  ", end="")
            #记录用户的操作
            weapon[1] = input();
            #str.isdigit()用于判断string是否能转换为int，避免用户输入错误时程序报错终止
            if not weapon[1].isdigit():
                est = 1
                os.system("cls")
                print("\t\t    >>>您的输入有误<<<")
                continue
            weapon[1] = int(weapon[1])
            #用户输入给出值以外的数据报错
            if weapon[1] != 1 and weapon[1] != 2 and weapon[1] != 3 and weapon[1] != 4:
                est = 1
                os.system("cls")
                print("\t\t    >>>您的输入有误<<<")
                continue
            #记录完用户输入的数据后进行下一步操作
            os.system("cls")
        #武器品质输入
        est = 1
        while est:
            #默认下一次不会再进入循环
            est = 0;
            #界面
            print("=================欢迎使用武器仓库管理系统=================")
            print("\n\t--------------   添加武器   --------------")
            print("\n\t              请输入武器职业")
            print("\n\t\t       <1> 普通 白")
            print("\t\t       <2> 精良 绿")
            print("\t\t       <3> 稀有 蓝")
            print("\t\t       <4> 史诗 紫")
            print("\t\t       <5> 传说 橙")
            print("\t\t       <6> 绝世 红")
            print("\t\t       <7> 不详 黑")
            print("\n\t\t     >>>  ", end="")
            #记录用户的输入
            weapon[2] = input();
            #str.isdigit()用于判断string是否能转换为int，避免用户输入错误时程序报错终止
            if not weapon[2].isdigit():
                est = 1
                os.system("cls")
                print("\t\t    >>>您的输入有误<<<")
                continue
            #判断用户输入的操作 ，并执行相对应的记录
            #若用户输入列表以外的数据，默认为7
            weapon[2] = int(weapon[2])
            if weapon[2] < 0 or weapon[2] > 7:
                est = 1
                os.system("cls")
                print("\t\t    >>>您的输入有误<<<")
                continue
            #记录完用户输入的数据后进行下一步操作
            os.system("cls")
        #武器伤害输入
        est = 1
        while est:
            #默认下一次不会再进入循环
            est = 0;
            #界面
            print("=================欢迎使用武器仓库管理系统=================")
            print("\n\t--------------   添加武器   --------------")
            print("\n\t       请输入武器攻击伤害(0 ~ 999)")
            print("\n\t\t     >>>  ", end="")
            #记录用户的输入
            weapon[3] = input();
            #str.isdigit()用于判断string是否能转换为int，避免用户输入错误时程序报错终止
            if not weapon[3].isdigit():
                est = 1
                os.system("cls")
                print("\t\t    >>>您的输入有误<<<")
                continue
            #判断用户输入的操作 ，并执行相对应的记录
            #输入为字符串类型，转换为int型
            weapon[3] = int(weapon[3])
            if weapon[3] > 999 or weapon[3] < 0:
                est = 1
                os.system("cls")
                print("\t\t    >>>您的输入有误<<<")
            #记录完用户输入的数据后进行下一步操作
            else:
                os.system("cls")
        #武器伤害攻速
        est = 1
        while est:
            #默认下一次不会再进入循环
            est = 0;
            #界面
            print("=================欢迎使用武器仓库管理系统=================")
            print("\n\t--------------   添加武器   --------------")
            print("\n\t         请输入武器攻击速度(每秒)")
            print("\n\t\t     >>>  ", end="")
            #记录用户的输入
            weapon[4] = input();
            #str.isdigit()用于判断string是否能转换为int，避免用户输入错误时程序报错终止
            if not weapon[4].isdigit():
                est = 1
                os.system("cls")
                print("\t\t    >>>您的输入有误<<<")
                continue
            #判断用户输入的操作 ，并执行相对应的记录
            #输入为字符串类型，转换为int型
            weapon[4] = int(weapon[4])
            if weapon[4] > 999 or weapon[4] < 0:
                est = 1
                os.system("cls")
                print("\t\t    >>>您的输入有误<<<")
            #记录完用户输入的数据后进行下一步操作
            else:
                os.system("cls")
        #武器伤害距离
        est = 1
        while est:
            #默认下一次不会再进入循环
            est = 0;
            #界面
            print("=================欢迎使用武器仓库管理系统=================")
            print("\n\t--------------   添加武器   --------------")
            print("\n\t         请输入武器攻击距离(厘米)")
            print("\n\t\t     >>>  ", end="")
            #记录用户的输入
            weapon[5] = input();
            #str.isdigit()用于判断string是否能转换为int，避免用户输入错误时程序报错终止
            if not weapon[5].isdigit():
                est = 1
                os.system("cls")
                print("\t\t    >>>您的输入有误<<<")
                continue
            #判断用户输入的操作 ，并执行相对应的记录
            #输入为字符串类型，转换为int型
            weapon[5] = int(weapon[5])
            if weapon[5] > 99999 or weapon[5] < 0:
                est = 1
                os.system("cls")
                print("\t\t    >>>您的输入有误<<<")
            #记录完用户输入的数据后进行下一步操作
            else:
                os.system("cls")
        #武器暴击几率
        est = 1
        while est:
            #默认下一次不会再进入循环
            est = 0;
            #界面
            print("=================欢迎使用武器仓库管理系统=================")
            print("\n\t--------------   添加武器   --------------")
            print("\n\t         请输入武器暴击几率(0~100)")
            print("\n\t\t     >>>  ", end="")
            #记录用户的输入
            weapon[6] = input();
            #str.isdigit()用于判断string是否能转换为int，避免用户输入错误时程序报错终止
            if not weapon[6].isdigit():
                est = 1
                os.system("cls")
                print("\t\t    >>>您的输入有误<<<")
                continue
            #判断用户输入的操作 ，并执行相对应的记录
            #输入为字符串类型，转换为int型
            weapon[6] = int(weapon[6])
            if weapon[6] > 100 or weapon[6] < 0:
                est = 1
                os.system("cls")
                print("\t\t    >>>您的输入有误<<<")
            #记录完用户输入的数据后进行下一步操作
            else:
                os.system("cls")
        #武器战力
        #计算公式：[(基础伤害 * 非暴击几率百分比) + (暴击伤害 * 暴击率百分比)] * 攻击速度 * sqrt(攻击距离)
        weapon[7] = ((weapon[3] * (weapon[6] / 100)) + (weapon[3] * 2 * (1 - weapon[6] / 100))) * weapon[4] * math.sqrt(weapon[5])
        #打开武器库文件，准备写入信息 a为追加模式
        f = open("weapon.txt", "a")
#判断武器文件和密码文件是否存在，若不存在则创建
if not os.path.exists("password.txt"):
    # w 只用于写入，如果该文件已存在则覆盖，不存在则创建。
    f = open("password.txt", "w")
    f.close()
if not os.path.exists("weapon.txt"):
    f = open("weapon.txt", "w")
    f.close()
'''
info = ["星辰之龙", 3, 5, 100, 1, 100, 0.5, 1500]
w = Weapon(info)
h = House()
w.output()
'''
h = House()

os.system("pause");
os.system("cls");  #结束前清屏
print("===感谢使用===")
os.system("pause");