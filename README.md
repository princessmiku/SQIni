# SQIni
The purpose of this package is to have a simple method of revising tables in a SQLite database. It is also possible to convert current tables as ini files.

There is a protection that prevents you from deleting data by removing something from the ini

The following options can currently be used, the others are not functional
- ``sqini.Database()``
- ``read()``
- ``syncToDatabase()``
- ``syncToIni()``
- ``.db``


### Install the pip

```
pip install sqini
```

## How to use

Import SQIni in your script

```python
import sqini
```

### define SQIni

```python
import sqini

database = sqini.Database() # enter the configurations here (iniSync, canDelete)
database.read('database path') #here you have to specify the database and the path
```

### Setup the sync from a ini file with your sqlite database

A SQLite databse must endig with `.db`.

The ini file must have the same name as the sqlite database, it is found automatically when reading, if none is available one is created.
If no path to a database is given, a database is created once. However, it will not be read in automatically when the program is started again.

example script
```python
import sqini
database = sqini.Database()
database.read('./mydata.db')
database.syncToDatabase()
```

There is a security that prevents files from being deleted should an entry be removed from the ini file. This can be switched off with `canDelete = True` when initializing-

Important! If the file is in the same directory put a `. /` In front, this is required, otherwise the path is missing. If another path is specified, it does not have to be specified


### Sync your current database with a ini file

Safety first, for syncing a database with a ini you need allow it with `iniSync=True`, it should protect against unintentional editing

if you do not allow it, a warning message will appear and it will not be carried out
```python
import sqini
database = sqini.Database(iniSync=True)
database.read('./mydata.db')
database.syncToIni()
```

### Use the normal database

it is also possible to control the database via sqlite3 without having to define it again

As example with execute. The `db` variable is the normal sqlite3 connection.
```python
import sqini
database = sqini.Database(iniSync=True)
database.read('./mydata.db')

database.db.execute() # as example
```


# THE INI FILE
the ini file must have the same name as the database, only it must end with `.ini`. You do not have to specify this when reading in because it derives it

An ini file is structured as follows so that it works

Always only **ONE** space as spacing, otherwise errors will occur. In the `default_value` this does not matter if you use a string.

If you do something wrong, no data will be damaged, there will be an error beforehand.
```ini
[user]
id = INTEGER 0 0 0 0
name = TEXT 0 0 0 0 'unbekannt'
money = INTEGER 0 0 0 0 1000
inventory = TEXT 0 0 0 0 '{}'
description = TEXT 0 0 0 0
```

construction

- `[user]` - that's the table name - *you can enter what you want here*
- `id`, `name` - that's the column name - *you can enter what you want here*
- Types - SQLite databases are of different types, all of which can be used
- Numbers, Here are 4 numbers, these mean in sequence `not_null`, `primary_key`, `autoincerment` and `unique`. `0` is deactivated and `1` is activated.
- The last is the default value that the column should have.
  If you don't want to specify anything, don't write anything. Otherwise, write your desired value as a string with `'your string'` and a number like `598` or `2985.123`.
  
### SQLite Types

- `INTEGER` - to save numbers
- `TEXT` - to save text/strings
- `BLOB`, `REAL`, `NUMERIC`