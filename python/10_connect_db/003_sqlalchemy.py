# SQLAlchemy 示例
#
# 运行方式：
#     python 10_connect_db/003_sqlalchemy.py
#
# 这个示例默认使用 SQLite，避免学习 ORM 时被 MySQL 服务配置卡住。
# 如果要连接 MySQL，只需要把 create_engine 的连接字符串换成 mysql+mysqlconnector://...

from pathlib import Path


CURRENT_DIR = Path(__file__).resolve().parent
DB_FILE = CURRENT_DIR / "study_sqlalchemy.db"


def main() -> None:
    """演示 SQLAlchemy 的建表、插入和查询。"""

    try:
        from sqlalchemy import Column, Integer, String, create_engine, select
        from sqlalchemy.orm import DeclarativeBase, Session
    except ImportError:
        print("未安装 SQLAlchemy，请先执行：pip install SQLAlchemy")
        return

    class Base(DeclarativeBase):
        """所有 ORM 模型的基类。"""

    class User(Base):
        """用户表模型。"""

        __tablename__ = "user"

        id = Column(Integer, primary_key=True, autoincrement=True)
        name = Column(String(20), nullable=False)

        def __repr__(self) -> str:
            return f"User(id={self.id}, name={self.name!r})"

    # echo=True 会打印 SQL，学习 ORM 时有助于理解底层执行了什么语句。
    engine = create_engine(f"sqlite:///{DB_FILE}", echo=False)

    # 创建所有继承 Base 的表。真实项目建议使用 Alembic 管理迁移。
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        # 查询是否已存在同名用户，避免重复运行不断插入重复数据。
        exists = session.scalar(select(User).where(User.name == "John"))

        if exists is None:
            session.add(User(name="John"))
            session.commit()

        users = session.scalars(select(User)).all()

    print(f"数据库文件: {DB_FILE}")
    print(f"查询结果: {users}")


if __name__ == "__main__":
    main()
