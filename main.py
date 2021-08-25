import sqini

database = sqini.Database(iniSync=True, canDelete=True); database.read("./testDatabase.db")
#database.syncToIni()
database.syncToDatabase()
#database.add_column("byebye", "nothing here", "TEXT")
