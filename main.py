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

#创建武器个体类，用于输出武器信息
class Weapon:
    #构造函数
    def __init__(self, info):
        self.name = info[0]         #武器名称
        #注意 1 和 '1' 的区别
        self.career = (int)(info[1])       #武器职业
        self.quality = (int)(info[2])      #武器品质
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
        print("\t\t|     战力: %-10s\t|"%(str(self.power)))
        print("\t\t|     伤害: %-10s\t|"%(str(self.damage)))
        print("\t\t|     速度: %-10s\t|"%(str(self.speed)))
        print("\t\t|     距离: %-10s\t|"%(str(self.range)))
        print("\t\t|     暴击: %-10s\t|"%(str(self.crit)))
#此类用于从文件中读取武器信息，存入list1[][]中并返回
class ReadWeapon:
    def __init__(self) -> None:
        pass

    def readweapon(self) -> list:
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
        return list1
#此类写用户操作的主体
class House:
    #构造方法，进入登入方法
    def __init__(self):
        os.system("cls")  #运行前清屏
        self.login()
    #此方法用于用户登录
    def login(self):  
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
    #若首次使用即password文件中密码为空，则进入创建管理员密码方法
    def firstlogin(self,f):
        print("=================欢迎使用武器仓库管理系统=================")
        print("\n\t-------- 首次使用需创建管理员密码 ---------")
        print("\t\t       - 输入密码 -")
        print("\n\t\t     >>>  ", end="")
        temp_password = input()
        f.write(temp_password)
        self.password = temp_password
        os.system("cls")  #运行后清屏
    #具体功能菜单界面，用户选择进行操作
    def house(self):
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
                    self.house()
                case 2:
                    os.system("cls")
                    self.delWeapon()
                    self.house()
                case 3:
                    os.system("cls")
                    self.modWeapon()
                    self.house()
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
    #第一个功能，添加武器            
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
                os.system("cls")
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
                #通过ReadWeapon类中readweapon()来读取文件中武器信息
                list1 = ReadWeapon().readweapon()
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
            print("\n\t       请输入武器攻击伤害(0 ~ 9999)")
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
        weapon[7] = (int)(((weapon[3] * (weapon[6] / 100)) + (weapon[3] * 2 * (1 - weapon[6] / 100))) * weapon[4] * math.sqrt(weapon[5]))
        #打开武器库文件，准备写入信息 a为追加模式,以utf-8打开防止乱码
        f = open("weapon.txt", "a", encoding="utf-8")
        for i in range(0, 8):
            f.write((str)(weapon[i]))
            f.write(" ")
        f.write("\n")
        #文件用完及时关闭
        f.close()
        #进入下一步前清屏
        os.system("cls")
        #添加成功
        print("\t\t      >>>添加成功<<<")
    #第二个功能，删除武器库中的武器
    def delWeapon(self):
        #est用于判断以下输入操作是否合法，若不合法，通过while循环来重新输入
        #武器名输入
        est = 1;
        while est:
            #默认下一次会再进入循环
            #界面
            print("=================欢迎使用武器仓库管理系统=================")
            print("\n\t--------------   删除武器   --------------")
            print("\n\t              请输入武器名称")
            print("\t             - 输入off返回 -")
            print("\n\t\t     >>>  ", end="")
            weaponname = input();
            # 判断用户是否想返回
            if weaponname == "off" or weaponname == "OFF":
                os.system("cls")
                return;
            #通过Weapon类中武器信息读取函数来获取文件中武器信息
            list1 = ReadWeapon().readweapon()
            #循环判断用户输入的名字是否存在
            for i in range(0,len(list1)):
                if list1[i][0] == weaponname:
                    #检测到武器存在，修改判断条件，不进入下次循环
                    est = 0
                    break        
            if est == 1:
                #清屏重新显示
                os.system("cls")
                #提示输入错误
                print("\t\t >>>该名称的武器不存在<<<")
            else:
                os.system("cls")
                #界面
                print("=================欢迎使用武器仓库管理系统=================")
                print("\n\t--------------   武器详情   --------------\n")
                #通过Weapon类输出武器详情信息
                Weapon(list1[i]).output()
                print("\n\t\t 是否确认删除(Y/N):", end="")
                YorN = input()
                if YorN == 'Y' or YorN == 'y':
                    # w 只用于写入，如果该文件已存在则覆盖，不存在则创建。
                    f = open("weapon.txt", "w", encoding="utf-8")
                    for x in range(0, len(list1)):
                        if x != i:
                            for y in range(0, 8):
                                f.write((str)(list1[x][y]))
                                f.write(" ")
                            f.write("\n")
                    #文件用完及时关闭
                    f.close()
                    os.system("cls")
                    print("\t\t      >>>删除成功<<<")
                else:
                    os.system("cls")
                    print("\t\t      >>>取消删除<<<")
    #第三个功能，修改武器的某个信息
    def modWeapon(self):
        #初始化武器信息的八个参数
        weapon = ["", "", "", "", "", "", "", ""];
        #est用于判断以下输入操作是否合法，若不合法，通过while循环来重新输入
        est = 1;
        while est:
            #默认下一次会再进入循环
            est = 1;
            #界面
            print("=================欢迎使用武器仓库管理系统=================")
            print("\n\t--------------   修改武器   --------------")
            print("\n\t              请输入武器名称")
            print("\t             - 输入off返回 -")
            print("\n\t\t     >>>  ", end="")
            weapon[0] = input();
            # 判断用户是否想返回
            if weapon[0] == "off" or weapon[0] == "OFF":
                os.system("cls")
                return;
            #通过Weapon类中武器信息读取函数来获取文件中武器信息
            list1 = ReadWeapon().readweapon()
            #循环判断用户输入的名字是否存在
            for i in range(0,len(list1)):
                if list1[i][0] == weapon[0]:
                    #检测到武器存在，修改判断条件，不进入下次循环
                    est = 0
                    break;
            if est == 1:
                #清屏重新显示
                os.system("cls")
                #提示输入错误
                print("\t\t >>>该名称的武器不存在<<<")
            else:
                #清屏进入下一步
                os.system("cls")
        #est用于判断以下输入操作是否合法，若不合法，通过while循环来重新输入
        est = 1;
        while est:
            #默认下一次不会再进入循环
            est = 0;
            #界面
            print("=================欢迎使用武器仓库管理系统=================")
            print("\n\t--------------   武器详情   --------------\n")
            #通过Weapon类输出武器详情信息
            Weapon(list1[i]).output()
            print("\n       <1>武器名称     <2>武器职业     <3>武器品质")
            print("       <4>攻击伤害     <5>攻击攻速     <6>攻击距离")
            print("       <7>暴击几率     <0>取消修改")
            print("\n\t\t     >>>  ", end="")
            num = input()
            if not num.isdigit():
                est = 1
                os.system("cls")
                print("\t\t    >>>您的输入有误<<<")
                continue
            num = int(num)
            if num < 0 or num > 7:
                if num == 0:
                    os.system("cls")
                    return;
                est = 1
                os.system("cls")
                print("\t\t    >>>您的输入有误<<<")
            else:
                #进入下一步前清屏
                os.system("cls")
        match num:
            case 1:
                    #est用于判断以下输入操作是否合法，若不合法，通过while循环来重新输入
                    #武器名输入
                    est = 1;
                    while est:
                        #默认下一次不会再进入循环
                        est = 0;
                        #界面
                        print("=================欢迎使用武器仓库管理系统=================")
                        print("\n\t--------------   修改武器   --------------")
                        print("\n\t                 武器名称")
                        print("\t                2至4个汉字")
                        print("\n\t\t     >>>  ", end="")
                        weapon[0] = input();
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
                            #通过ReadWeapon类中readweapon()来读取文件中武器信息
                            list2 = ReadWeapon().readweapon()
                            for j in range(0,len(list2)):
                                if list2[j][0] == weapon[0]:
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
                    list1[i][0] = weapon[0]
            case 2:
                    est = 1
                    while est:
                        #默认下一次不会再进入循环
                        est = 0;
                        #界面
                        print("=================欢迎使用武器仓库管理系统=================")
                        print("\n\t--------------   修改武器   --------------")
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
                    list1[i][1] = weapon[1]
            case 3:
                    est = 1
                    while est:
                        #默认下一次不会再进入循环
                        est = 0;
                        #界面
                        print("=================欢迎使用武器仓库管理系统=================")
                        print("\n\t--------------   修改武器   --------------")
                        print("\n\t              请输入武器品质")
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
                    list1[i][2] = weapon[2]
            case 4:
                    est = 1
                    while est:
                        #默认下一次不会再进入循环
                        est = 0;
                        #界面
                        print("=================欢迎使用武器仓库管理系统=================")
                        print("\n\t--------------   修改武器   --------------")
                        print("\n\t       请输入武器攻击伤害(0 ~ 9999)")
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
                    list1[i][3] = weapon[3]
            case 5:
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
                    list1[i][4] = weapon[4]
            case 6:
                    est = 1
                    while est:
                        #默认下一次不会再进入循环
                        est = 0;
                        #界面
                        print("=================欢迎使用武器仓库管理系统=================")
                        print("\n\t--------------   修改武器   --------------")
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
                    list1[i][5] = weapon[5]
            case 7:
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
                    list1[i][6] = weapon[6]
        #武器战力
        #计算公式：[(基础伤害 * 非暴击几率百分比) + (暴击伤害 * 暴击率百分比)] * 攻击速度 * sqrt(攻击距离)
        list1[i][7] = (int)((((int)(list1[i][3]) * ((int)(list1[i][6]) / 100)) + ((int)(list1[i][3]) * 2 * (1 - (int)(list1[i][6]) / 100))) * (int)(list1[i][4]) * math.sqrt((int)(list1[i][5])))
        '''
            修改武器信息的方法：
            1.删除要修改的武器信息
            2.增加修改后的武器信息
        '''
        # w 只用于写入，如果该文件已存在则覆盖，不存在则创建。
        f = open("weapon.txt", "w", encoding="utf-8")
        for x in range(0, len(list1)):
            if x != i:
                for y in range(0, 8):
                    f.write((str)(list1[x][y]))
                    f.write(" ")
                f.write("\n")
                    #文件用完及时关闭
        f.close()
        #打开武器库文件，准备写入信息 a为追加模式,以utf-8打开防止乱码
        f = open("weapon.txt", "a", encoding="utf-8")
        for j in range(0, 8):
            f.write((str)(list1[i][j]))
            f.write(" ")
        f.write("\n")
        #文件用完及时关闭
        f.close()
        #进入下一步前清屏
        os.system("cls")
        #添加成功
        print("\t\t      >>>修改成功<<<")
#判断武器文件和密码文件是否存在，若不存在则创建，确保程序的正确运行
if not os.path.exists("password.txt"):
    # w 只用于写入，如果该文件已存在则覆盖，不存在则创建。
    f = open("password.txt", "w")
    f.close()
if not os.path.exists("weapon.txt"):
    f = open("weapon.txt", "w")
    f.close()
#实例化House对象，用户将进入操作界面
h = House()
#操作完结束程序
os.system("cls");  #结束前清屏
print("===感谢使用===")
os.system("pause");