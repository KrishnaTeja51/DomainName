import sqlite3

filename = str(input("Enter file name:"))
filename = "D:/" + filename
count = [0,0,0,0,0,0,0,0,0,0]

with open(filename,"r") as File:
    for line in File:
        if "iupui.edu" in line:
            count[0]+=1
        elif "umich.edu" in line:
            count[1]+=1
        elif "indiana.edu" in line:
            count[2]+=1
        elif "caret.cam.ac.uk" in line:
            count[3]+=1
        elif "vt.edu" in line:
            count[4]+=1
        elif "uct.ac.za" in line:
            count[5]+=1
        elif "media.berkeley.edu" in line:
            count[6]+=1
        elif "ufp.pt" in line:
            count[7]+=1
        elif "gmail.com" in line:
            count[8]+=1
        elif "et.gatech.edu" in line:
            count[9]+=1

db = sqlite3.connect(":memory:")

cursor = db.cursor()

cursor.execute('''
create table counts(
org varchar(50),
count integer
)''')

cursor.execute("delete from counts")

cursor.execute("insert into counts(org,count) values(\"iupui.edu\"," + str(count[0]) + ")")
cursor.execute("insert into counts(org,count) values(\"umich.edu\"," + str(count[1]) + ")")
cursor.execute("insert into counts(org,count) values(\"indiana.edu\"," + str(count[2]) + ")")
cursor.execute("insert into counts(org,count) values(\"caret.cam.ac.uk\"," + str(count[3]) + ")")
cursor.execute("insert into counts(org,count) values(\"vt.edu\"," + str(count[4]) + ")")
cursor.execute("insert into counts(org,count) values(\"uct.ac.za\"," + str(count[5]) + ")")
cursor.execute("insert into counts(org,count) values(\"media.berkeley.edu\"," + str(count[6]) + ")")
cursor.execute("insert into counts(org,count) values(\"ufp.pt\"," + str(count[7]) + ")")
cursor.execute("insert into counts(org,count) values(\"gmail.com\"," + str(count[8]) + ")")
cursor.execute("insert into counts(org,count) values(\"et.gatech.edu\"," + str(count[9]) + ")")

cursor.execute("select * from counts")

rows = cursor.fetchall()

for row in rows:
    print(row)

db.commit()
db.close()