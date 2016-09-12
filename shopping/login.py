#_*_ coding:utf-8 _*_
'''信用卡登录程序'''
def login(Info_path):
    #设定计数器
    count = 0
    #设定用户字典，用户锁定字典
    userdb = {}
    userLockInfo = {}
    userfile = Info_path+'.txt'
    #读取用户信息
    with open(userfile) as f:
        for line in f:
            username = line.split()[0]
            userdb[username] = line.split()[1]
            userLockInfo[username] = line.split()[2]
       
    while count < 3:
        print "------Please Login:---------"
        name = raw_input("User:")
        password = raw_input("Password:")
        if name not in userdb.keys():
            print "Your name or password is wrong!"
            continue
        if userLockInfo[name] == 'y':
            print "[505]User is Locked. Please phone to 110!"
            break
        if password == userdb[name]:
            print "Login Successfully!"
            break
        count+=1
        print "Your name or password is wrong!"
    else:
        count == 3
        userLockInfo[name]='y'
        print "User is Locked. Please phone to 110!"
    
    sfhandle = open(userfile,'w')
    for savename in userdb.keys():
        sfhandle.write(savename+'  '+userdb[savename]+'  '+userLockInfo[savename]+'\n')
       
    sfhandle.close()
    return name,userLockInfo[name]    
