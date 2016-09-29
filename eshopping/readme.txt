程序说明：
功能：实现购物、结算、信用卡管理等常见网上商城购物流程
v1：函数式流程：

1. 购物（Shopping)   #登录购物账户（shopping_userdb） 
1.1 购物 1.2 清空购物车 3. 结算 4.个人中心（绑定信用卡，购物日志)
文件：商品信息（goodsdb）购物账户（shopping_userdb） 绑定文件（userbind） 购物车目录（cartdb）日志（recordlog）

2. 信用卡（CreditCard） #登陆信用卡账户 （carduserdb）
2.1 我的信用卡 2.2 提现 2.3 转账 2.4 还款 2.4 流水记录 
文件：信用卡信息（cardinfo）  

3. 后台管理（BackendAdmin）#登陆管理员账户
3.1 购物账户管理（创建账户，锁定账户，解锁账户）
3.2 信用卡账户管理（绑定信用卡，锁定信用卡，解锁信用卡，提升额度）



20116.9.12
	增加‘信用卡处理功能’，展示，遇到困难（如何处理用户信用卡信息）修改信用卡内额度限制，更改信用卡信息普通文本为json样式，学习json处理文本（dump,load)
	展示信息和修改信息changeCardInfo，通过默认参数的形式达到一个函数两个目的（显示或修改）
2016.9.13
	增加 取现，还款功能，学习关注格式化输出print format
2016.9.15
	完成CreditCard大部分功能，
	重新编写购物中心功能，序列化购物商品清单
2016.9.16
	修改Login，登录失败时返回False
	绑定信用卡账户和购物账户，完成付款流程
2016.9.20
	完善后台管理部分
2016.9.21
	重新梳理软件功能	
2016.9.22
	程序优化目录结构：
│  index.py
│  readme.txt
│  __init__.py
│
├─config
│      __init__.py
│
├─database
│      cardinfo.txt
│      carduserdb.txt
│      cartdb.txt
│      goodsdb.txt
│      recordlog
│      recordlog.txt
│      shopping_userdb.txt
│      userbind.txt
│
└─modules
        backendAdmin.py
        backendAdmin.pyc
        creditCard.py
        creditCard.pyc
        login.py
        login.pyc
        personalcenter.py
        select.py
        select.pyc
        shopping.py
        shopping.pyc
        __init__.py	

	根据新目录结构修改程序

2016.9.27
	采用sqlite3数据库，学习数据库编程部分，重新编写程序
2016.9.29
	初步完善程序中sqlite3数据库操作
	修改程序文件结构为 模块modules，数据操作utility，配置config
│  .gitignore
│  config.py
│  index.py
│  readme.txt
│  __init__.py
│
├─modules
│      backendAdmin.py
│      creditCard.py
│      login.py
│      login.pyc
│      personalcenter.py
│      select.py
│      shopping.py
│      __init__.py
└─utility
        DBhandle.py
        eshopping.db3
        sqlhandle.py
        __init__.py