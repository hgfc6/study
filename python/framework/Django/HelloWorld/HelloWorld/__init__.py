# import pymysql
# pymysql.install_as_MySQLdb()

import sqlite3
from pathlib import Path
sqlite3.connect(Path(__file__).parent.parent / 'db.sqlite3')