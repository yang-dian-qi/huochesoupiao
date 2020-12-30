import pymssql #引入pymssql模块
zhanghao='sa'
mima='www.ydq2244'
def xiugai():
    sql="SELECT * FROM Customer WHERE Unumber=" + zhanghao
    print("您的基本信息如下：")
    print("Unumber    Uname    password  Adress       Cnumber          Pnumber")
    try:
        cur.execute(sql)  # 执行单条的sql语句，
        res = cur.fetchone()
        for i in range(len(res)):  # 输出
            if i == len(res) - 1:
                print(res[i])
            else:
                print(res[i], end=' ')
    except:
        print("输入格式有问题")
    while 1:
        print("请输入您要修改的属性或者退出修改个人信息")
        print("1：Uname   2：Adress   3：Cnumber   4：Pnumber   5：退出修改个人信息")
        m = input()
        if m == '1':
            print("请输入修改后的值：")
            n = input()
            sql = "UPDATE Customer set Uname=" + n + " WHERE Unumber=" + zhanghao
            cur.execute(sql)
            conn.commit()
            print("修改成功")
        elif m == '2':
            print("请输入修改后的值：")
            n = input()
            sql = "UPDATE Customer set Adress=" + n + " WHERE Unumber=" + zhanghao
            cur.execute(sql)
            conn.commit()
            print("修改成功")
        elif m == '3':
            print("请输入修改后的值：")
            n = input()
            sql = "UPDATE Customer set Cnumber=" + n + " WHERE Unumber=" + zhanghao
            cur.execute(sql)
            conn.commit()
            print("修改成功")
        elif m == '4':
            print("请输入修改后的值：")
            n = input()
            sql = "UPDATE Customer set Pnumber=" + n + " WHERE Unumber=" + zhanghao
            cur.execute(sql)
            conn.commit()
            print("修改成功")
        elif m == '5':
            return
        else:
            print("输入错误！请重新输入！")
def chakan():
    sql = "SELECT * FROM Dindan WHERE Unumber=" + zhanghao
    print("您的订单信息如下：")
    try:
        cur.execute(sql)  # 执行单条的sql语句，
        while 1:
            res = cur.fetchone()  # 获取游标所在处的一行数据，返回元组
            if res is None:  # 结果已经取完了
                break
            for i in range(len(res)):  # 输出
                if i == len(res) - 1:
                    print(res[i])
                    break
                print(res[i], end=' ')
    except:
        print("输入格式有问题")
    while 1:
        print("您可以选择删除自己的购票记录或者返回初始页面：")
        print("1：删除购票记录   2：返回初始页面")
        m=input()
        if m=='1':
            print("请输入您要删除的订单编号：")
            n=input()
            sql="DELETE FROM Dindan WHERE Onumber=" + n + " AND Unumber="+ zhanghao
            cur.execute(sql)
            conn.commit()
            print("删除成功!")
        elif m=='2':
            return
        else:
            print("输入错误！请重新输入！")
def goupiao():
    print("请输入您的出发地和目的地：")
    m=str(input("请输入出发地："))
    n=str(input("请输入目的地："))
    sql = "SELECT * FROM Train WHERE Tnumber ='T333'"
    cur.execute(sql)  # 执行单条的sql语句，
    print("符合您选择的列车信息有：")
    while 1:
        res = cur.fetchone()  # 获取游标所在处的一行数据，返回元组
        if res is None:  # 结果已经取完了
            break
        for i in range(len(res)):  # 输出
            if i == len(res) - 1:
                print(res[i])
                break
            print(res[i], end=' ')
    print("确认您选择的列车编号,批次号：")
    x=input("请输入列车编号：")
    y=input("请输入批次号：")
    '''
    sql="INSERT INTO Dindan VALUES('000007','0001','T333','长沙','武汉','普通列车','二','2018.12.07')"
    cur.execute(sql)
    '''
    cur.execute("insert into Dindan(Onumber,Unumber,Tnumber,Start,FInish,Models,Seat,TIme) values('004567','0001','T333','changsha','wuhan','putong','二','2018.12.07')")
    conn.commit()
    print("提交订单成功！")
    return
while 1:  # 输入用户名和密码来登录数据库
    print("-----------------欢迎使用火车售票管理系统------------------")
    zhanghao = input("请输入您的账号：")
    mima = input("请输入您的密码：")
    try:
        conn = pymssql.connect(host='(local)', user=zhanghao, password=mima, database='huochesoupiao',charset='cp936')  # 服务器名,账户,密码,数据库名
        cur = conn.cursor()  # 获取光标
        print("登录成功")
        break
    except:
        print("账号或密码错误，请重新输入")
print("请选择您的操作：")
while 1:
    print("----------------------")
    print("1：修改自己的个人信息     |")
    print("2：查看自己曾经的购票记录  |")
    print("3：购票                |")
    print("4：退出火车购票系统       |")
    print("----------------------")
    m = int(input("请输入您选择的操作："))
    if m == 1:
        xiugai()
    elif m == 2:
        chakan()
    elif m == 3:
        goupiao()
    elif m==4:
        break
    else:
        print("请输入正确的选择！")
cur.close()
conn.close()
print("已退出火车售票管理系统！欢迎下次使用！")
