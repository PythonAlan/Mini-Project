修改haproxy配置文件

博客:http://www.cnblogs.com/alan-babyblog/p/5181156.html

基本功能:
1.获取记录
2.添加记录
3.删除记录

代码结构:
三个函数一个主函数

知识点:
1.python简单数据结构的使用：列表、字典等

2.python两个模块的使用：os和json

　　　　　　a.os.rename('文件1'，'文件2')

　　　　　　b.json完成自动识别字典、列表，并识别后进行自动转换

3.python函数的定义和调用

4.标志位的灵活运用：flag和haswrite分别用于找backend的record和判断是否已经将记录写入到文件

5.python基本语法的使用:for循环、if...else....判断

6.python文件的操作的基本使用：with open('文件1','模式') as obj1,open('文件2','模式') as obj2

