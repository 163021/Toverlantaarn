import pandas
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Toverlantaarn"
)

mycursor = mydb.cursor()

df = pandas.read_csv('Museum-collectie-beschrijving.csv')

# print(df)

# for item in range(0, 44):
#     # print(df[item])
#     sql = "INSERT INTO lantaarn (Objectcode) VALUES (%s)"
#     val = (df['Objectcode'][4])
#     print(val)
#     mycursor.execute(sql, val)
#     mydb.commit()
#     print(mycursor.rowcount, "record inserted.")

# for item in range(0, 44):
#     # print(df[item])
#     sql = "INSERT INTO lantaarn (Objectcode, Object, Categorie, Type, Unnamed, Afmeting, Beschrijving, Operationeel, Conditie, Foto) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
#     val = (df['Objectcode'][0], df['Object'], df['Categorie'], df['Type'], df['Unnamed: 4'], df['Afmeting'], df['Beschrijving'], df['operationeel'], df['Conditie'], df['Foto'])
#     mycursor.execute(sql, val)
#     mydb.commit()
#     print(mycursor.rowcount, "record inserted.")
