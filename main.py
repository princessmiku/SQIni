import sqini

database = sqini.Database(iniSync=True, canDelete=True); database.read("./testDatabase.db")
database.syncToDatabase()
