import pymysql

db = pymysql.connect(host='localhost', user='root', password='151934', port=3306, db='webspider')

cursor = db.cursor()
sql = 'CREATE TABLE IF NOT EXISTS TXjob (id VARCHAR(255) NOT NULL, name VARCHAR(255) NOT NULL , type VARCHAR(255) NOT NULL, num VARCHAR(255) NOT NULL , site VARCHAR(255) NOT NULL , date VARCHAR(255) NOT NULL, PRIMARY KEY(id))'

cursor.execute(sql)

db.close()


