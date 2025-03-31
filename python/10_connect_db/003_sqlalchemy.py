from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

Base = declarative_base()
class User(Base):
    #表名
    __tablename__ = 'user'

    # 表结构
    id = Column(String(20), primary_key=True)
    name = Column(String(20))

# 初始化数据库连接:
engine = create_engine('mysql+mysqlconnector://root:123456@localhost:3306/cjh')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

# 插入数据
# session = DBSession()
# session.add(User(id='2', name='John'))
# session.commit()
# session.close()

# 查询
session = DBSession()
user = session.query(User).filter(User.id=='2').one()
print(type(user))
print(user.name)
session.close()