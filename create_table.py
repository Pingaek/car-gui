sql = '''
  create table car(
    id integer primary key,
    pokemon text not null,
    element text not null,
    gen integer not null,
    price integer not null
  );
'''

from db_connect import db, cursor
cursor.execute(sql)
db.commit()
