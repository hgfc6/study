# Python定义了一套操作数据库的API接口，任何数据库要连接到Python，只需要提供符合Python标准的数据库驱动即可
# Connection 一条数据库连接
# Cursor 游标，拿到连接打开游标才能开始执行数据库操作

# python自带sqlite
import sqlite3

conn = sqlite3.connect('test.db')  # 文件不存在会新建
cursor = conn.cursor()
cursor.execute('select * from user where name=? and pwd=?', ('abc', 'password'))# ？占位，元组赋值
cursor.rowcount  #增删改影响行数
cursor.fetchall() # 查询结果

# 提交事务
conn.commit()
# 一定记得关闭cursor和connection(try except finally)
cursor.close()
conn.close()
