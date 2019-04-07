import pymysql

db = pymysql.connect(host='localhost', user='root', password='151934', port=3306, db='ws0405')

cursor = db.cursor()
sql = 'CREATE TABLE IF NOT EXISTS TXjob (id INT(6) NOT NULL auto_increment, workName VARCHAR(255) NOT NULL , workType VARCHAR(255) NOT NULL, needNum int(5) NOT NULL , site VARCHAR(255) NOT NULL , duty message_text NOT NULL, requirement message_text NOT NULL ,PRIMARY KEY(id))'

cursor.execute(sql)

db.close()