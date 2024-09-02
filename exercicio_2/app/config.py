class Config:
    #SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://sa:123456@localhost/ENEM_2023?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://sa:123456@localhost:1433/ENEM_2023?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
