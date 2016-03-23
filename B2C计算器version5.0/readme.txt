myblog

http://www.cnblogs.com/alan-babyblog/p/5297025.html



dist 里面的就是可以使用app

构建发布版应用
当测试通过后，你可以通过调用 python setup.py py2app 来生成发布版。确保旧的 build 和 dist 文件类都被删除了：

$ rm -rf build dist
$ python setup.py py2app