import pandas as pd
import pyodbc
# import mysql.connector

# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="",
#     database="Toverlantaarn"
# )

server = 'localhost' 
database = 'Toverlantaarn' 
username = 'root' 
password = '' 
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

df = pd.read_csv("Museum-collectie-beschrijvinging.csv")

print(df)

for index, row in df.iterrows():
    cursor.execute("INSERT INTO Toverlantaarn.lantaarn (Objectcode, Object, Categorie, Type, Unnamed, Afmeting, Beschrijving, Operationeel, Conditie, Foto) values(?,?,?,?,?,?,?,?,?,?)", row.Objectcode, row.Object, row.Categorie, row.Type, row.Unnamed, row.Afmeting, row.Beschrijving, row.Operationeel, row.Conditie, row.Foto)
cnxn.commit()
cursor.close()

# for item in range(0, 44):
#     # print(df[item])
#     sql = "INSERT INTO lantaarn (Objectcode, Object, Categorie, Type, Unnamed, Afmeting, Beschrijving, Operationeel, Conditie, Foto) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
#     val = (df['Objectcode'][0], df['Object'], df['Categorie'], df['Type'], df['Unnamed: 4'], df['Afmeting'], df['Beschrijving'], df['operationeel'], df['Conditie'], df['Foto'])
#     mycursor.execute(sql, val)
#     mydb.commit()
#     print(mycursor.rowcount, "record inserted.")
