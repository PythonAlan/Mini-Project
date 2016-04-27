__author__ = 'uesr'

# 0代表返回上一级
#Q代表退出
#尝试用for循环来重构
province = {1:'1.广东', 2:'2.广西', 3:'3.浙江'}

gd_city = {1:'1.广州', 2:'2.佛山', 3:'3.深圳'}
gx_city = {1:'南宁', 2:'柳州', 3:'北海'}
zj_city = {1:'上海', 2:'宁波', 3:'温州'}

gz_district = {}
fs_district = {}
sz_district = {}

nn_district = {}
lz_district = {}
bh_district = {}

sh_district = {}
nb_district = {}
wz_district = {}


print (province[1])
print (province[2])
print (province[3]) #展示省份

second_level = int(input('请输入要查询的省份编号:'))   #第二级查询
if second_level == 1:         #判断查询编号
    print(gd_city[1])
    print(gd_city[2])
    print(gd_city[3])

elif second_level ==2:
    print('测试')

elif second_level == 3:
    print('测试')

else:
    print('请输入正确的省市区编号')










