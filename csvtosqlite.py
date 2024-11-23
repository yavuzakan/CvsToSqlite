import csv, sqlite3, os 
from datetime import datetime

check_file = os.path.isfile("data.db")

if check_file:
    os.remove("data.db")

   

con = sqlite3.connect("data.db") 
cur = con.cursor()
cur.execute("CREATE TABLE t (col1, col2,col3);") 
simdi = datetime.now()

with open('data.csv','r') as fin: # `with` statement available in 2.5+
    # csv.DictReader uses first line in file for column headings by default
    dr = csv.DictReader(fin,delimiter=";") # comma is default delimiter
    to_db = [(i['col1'], i['col2'] , simdi ) for i in dr]

cur.executemany("INSERT INTO t (col1, col2, col3) VALUES (?, ? , ?);", to_db)
con.commit()
con.close()