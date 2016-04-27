作者：陈昶骏   2016.1.20

#用户登录作业和多级菜单作业
#我这里将两个作业合并成了同一个作业进行完成，由于时间限制，功能定制不完全。
流程图不太会画，请老师见谅

我的流程中，用户登录分为 管理员(superuser) 和 普通用户(user)
管理员的权限：
	1.列出所有用户的信息			
	2.解锁被锁定的用户（输错三次密码被锁定）  已完成
	3.新增用户

普通用户的权限：
	1.列出自己的基本信息
	2.如果这个账号不用了，可以锁定自己，下次不再能登陆
	3.修改密码

基础框架已经完成，作业二：多级菜单的跳转就是在用户的各个功能中实现。
*用户信息存在当前目录的文件中，json格式，有任何更新或者新增，会对文件进行重写。
*并且全部重新制作方便内部搜索使用的索引字典（user_list），这里字典命名有点问题，后期会改掉
*由于时间有限，还有些功能正在实现过程中，不知道在交作业之前能完成多少。

操作指南：
一）普通用户登录
正常登陆：
	please input username:yh
	please input password:321
	Hello yh login successfully
	***********************
	1.modify passwd
	2.lock me
	3.my information
	4.logout
	***********************
	please input action id:
锁定操作：
	please input username:yh
	please input password:123
	key error
	you have 2 chance
	please input password:2
	key error
	you have 1 chance
	please input password:1
	key error
	you have 0 chance
	sorry,this user would be locked immediately
二）超级用户登陆
正常登陆：
	please input username:cj
	please input password:123
	Hello cj login successfully
	***********************
	1.add user
	2.unlocked user
	3.list user information
	4.logout
	***********************
	please input action id:
锁定操作：
	please input username:cj
	please input password:1
	key error
	you have 2 chance
	please input password:2
	key error
	you have 1 chance
	please input password:3
	key error
	you have 0 chance
	sorry,this user would be locked immediately	

三）功能实现
1.超级用户解锁操作
	please input username:cj
	please input password:123
	Hello cj login successfully
	***********************
	1.add user
	2.unlocked user
	3.list user information
	4.logout
	***********************
	please input action id:2
	superuser_unlocked_user
	+----+----------+----------+
	| id | username |   tag    |
	+----+----------+----------+
	| 2  |    yh    |  locked  |
	| 1  |    cj    | unlocked |
	+----+----------+----------+
	which user id you want to unlocked2
	make sure y/ny
	+----+----------+----------+
	| id | username |   tag    |
	+----+----------+----------+
	| 2  |    yh    | unlocked |
	| 1  |    cj    | unlocked |
	+----+----------+----------+
	press b,back to menu

2.超级用户打印所有用户信息列表
	please input username:cj
	please input password:123
	Hello cj login successfully
	***********************
	1.add user
	2.unlocked user
	3.list user information
	4.logout
	***********************
	please input action id:3
	superuser_list_info
	+----+----------+------+-----+----------+-----------+
	| id | username | name | age |   tag    | superuser |
	+----+----------+------+-----+----------+-----------+
	| 1  |    cj    | ccj  |  24 | unlocked |    yes    |
	| 2  |    yh    | xyh  |  25 | unlocked |     no    |
	+----+----------+------+-----+----------+-----------+
	press b,back to menu

3.超级用户实现新增用户
	please input username:cj
	please input password:123
	Hello cj login successfully
	***********************
	1.add user
	2.unlocked user
	3.list all of users' information
	4.logout
	***********************
	please input action id:1
	superuser_add_user
	input usernametll
	input passwd222
	please input nametangll
	please input age22
	do you want to set passwd question y/ny
	input questionfav_count
	input answerkorea
	continue input q&a? y/nn
	is this user is a superuser? y/ny
	press b,back to menub
	***********************
	1.add user
	2.unlocked user
	3.list all of users' information
	4.logout
	***********************
	please input action id:4
	please input username:tll
	please input password:222
	Hello tll login successfully
	***********************
	1.add user
	2.unlocked user
	3.list all of users' information
	4.logout
	***********************
	please input action id:3
	superuser_list_info
	+----+----------+--------+-----+----------+-----------+
	| id | username |  name  | age |   tag    | superuser |
	+----+----------+--------+-----+----------+-----------+
	| 1  |    cj    |  ccj   |  24 | unlocked |    yes    |
	| 2  |    yh    |  xyh   |  25 | unlocked |     no    |
	| 3  |   tll    | tangll |  22 | unlocked |    yes    |
	+----+----------+--------+-----+----------+-----------+
	press b,back to menu

