import sqini

database = sqini.Database(iniSync=True, canDelete=True); database.read("./dist/testDatabase.db")
#database.syncToIni()
database.syncToDatabase()
#database.add_column("byebye", "nothing here", "TEXT")