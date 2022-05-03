"""
练习：将单词本存入数据库
1.创建数据库 dict(utf8)
2.创建数据表 words 将单侧和单词解释分别存入不同的字段
3.编写程序，将单词村容words单词表 超过19500条即可
"""
import pymysql
import re

fd = open('dict.txt', 'r')

db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password='123456',
                     database='dict',
                     charset='utf8')

cur = db.cursor()

sql = "insert into words (word, mean) values (%s, %s);"

for line in fd:
    # 获取单词和解释
    tup = re.findall(r'(\S+)\s+(.*)', line)[0]
    try:
        cur.execute(sql, tup)
    except Exception as e:
        db.rollback()
        print(e)

db.commit()

fd.close()
cur.close()
db.close()
