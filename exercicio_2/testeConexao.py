import pyodbc

try:
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                          'SERVER=192.168.0.118,1433;'
                          'DATABASE=ENEM_2023;'
                          'UID=firstdecision;PWD=@tktp@123')
    print("Conexão estabelecida com sucesso!")
except pyodbc.Error as ex:
    print("Erro ao conectar:", ex)
