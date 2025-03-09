# 操作文件或者文件夹
# 注意：在Python中，操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中，这一点要注意一下

# 常用文件（夹）操作函数
# 1. os.path.join()：拼接路径
# 2. os.path.exists()：判断文件（夹）是否存在
# 3. os.path.isfile()：判断是否为文件
# 4. os.path.isdir()：判断是否为目录
# 5. os.path.getsize()：获取文件（夹）大小
# 6. os.path.getmtime()：获取文件（夹）最后修改时间
# 7. os.path.getatime()：获取文件（夹）最后访问时间
# 8. os.path.getctime()：获取文件（夹）创建时间
# 9. os.path.basename()：获取文件（夹）名
# 10. os.path.dirname()：获取文件（夹）所在目录
# 11. os.path.split()：拆分路径为目录和文件名
# 12. os.path.splitext()：拆分文件名为文件名和扩展名
# 13. os.path.abspath()：获取绝对路径
# 14. os.path.relpath()：获取相对路径
# 15. os.path.commonpath()：获取两个路径的公共部分
# 16. os.path.walk()：遍历目录树
# 17. os.path.expanduser()：展开用户目录
# 18. os.path.expandvars()：展开环境变量
# 19. os.path.normpath()：规范路径
# 20. os.path.samefile()：判断两个路径是否指向同一个文件
# 21. os.path.sameopenfile()：判断两个文件描述符是否指向同一个文件
# 22. os.path.samestat()：判断两个路径的状态是否相同
# 23. os.path.isabs()：判断路径是否为绝对路径
# 24. os.path.islink()：判断路径是否为符号链接
# 25. os.path.ismount()：判断路径是否为挂载点
# 26. os.path.lexists()：判断路径是否存在，包括符号链接
# 27. os.path.realpath()：获取符号链接的真实路径
# 28. os.path.supports_unicode_filenames()：判断是否支持Unicode文件名

# os.mkdir()：创建目录
# os.makedirs()：创建多层目录
# os.rmdir()：删除空目录
# os.remove()：删除文件
# os.unlink()：删除文件，与remove()相同
# os.rename()：重命名文件或目录
# os.renames()：重命名多层目录
# os.listdir()：列出目录内容
# os.stat()：获取文件（夹）状态信息
# os.chmod()：修改文件（夹）权限
# os.utime()：修改文件（夹）最后访问和修改时间

# 复制文件在os中不存在，可以使用shutil模块中的copyfile()函数
# 移动文件在os中不存在，可以使用shutil模块中的move()函数
# shutil有很多实用函数，可以实现文件（夹）的复制、移动、压缩、解压、重命名等操作
# 详情请参考：https://docs.python.org/3/library/shutil.html


# 一行代码筛选目录中的.py文件
import os
for name in [n for n in os.listdir('.') if os.path.isfile(n) and os.path.splitext(n)[1] == '.py']:
    print(name)