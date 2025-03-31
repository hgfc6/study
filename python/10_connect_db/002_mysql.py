import mysql.connector


try:
    conn = mysql.connector.connect(host="127.0.0.1", port=3306, user='root', password='123456', database='cjh')
    cursor = conn.cursor()
    cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
    # 插入一行记录，注意MySQL的占位符是%s:
    cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])
    conn.commit()
except Exception as e:
    print(e)
finally:
    cursor.close()
    conn.close()