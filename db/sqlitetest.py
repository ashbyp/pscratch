# https://docs.python.org/3/library/sqlite3.html
import sqlite3
import sqlalchemy
import os
import pandas as pd


def create_table(con):
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS padel
                   (date text, opponents text, us real, them real)''')
    cur.execute("INSERT INTO padel VALUES ('2022-07-22','Ben Moss',2, 1)")
    con.commit()


def read_from_table(con):
    cur = con.cursor()
    for row in cur.execute('SELECT * FROM padel ORDER BY date'):
        print(row)


def test_param_insertion(con):
    cur = con.cursor()
    cur.execute("create table if not exists lang (name, first_appeared)")
    cur.execute("insert into lang values (?, ?)", ("C", 1972))
    lang_list = [
        ("Fortran", 1957),
        ("Python", 1991),
        ("Go", 2009),
    ]
    cur.executemany("insert into lang values (?, ?)", lang_list)
    con.commit()

    cur.execute("select * from lang where first_appeared=:year", {"year": 1972})
    print(cur.fetchall())

    print('================')
    for row in cur.execute('select * from lang'):
        print(row)
    print('================')


def delete_db_file(filename):
    import os
    if os.path.exists(filename):
        os.remove(filename)
    else:
        print(filename)


def test_alchemy(filename):
    print(f'will connect to sqlite:///{filename}')
    engine = sqlalchemy.create_engine(f'sqlite:///{filename}', echo=True)
    connection = engine.connect()
    metadata = sqlalchemy.MetaData()
    padel = sqlalchemy.Table('padel', metadata, autoload=True, autoload_with=engine)
    print(padel.columns.keys())

    query = sqlalchemy.select([padel])
    proxy = connection.execute(query)
    rs = proxy.fetchall()
    print(rs[:3])

    df = pd.DataFrame(rs)
    print(df)

    lang = sqlalchemy.Table('lang', metadata, autoload=True, autoload_with=engine)
    query = sqlalchemy.select([lang]).where(lang.columns.name == 'Python')
    print('Execute lang query: ')
    proxy = connection.execute(query)
    rs = proxy.fetchall()
    print(rs)

    d = lang.delete()
    engine.execute(d)


def main():
    con = sqlite3.connect('example.db')
    create_table(con)
    read_from_table(con)
    test_param_insertion(con)
    con.close()
    test_alchemy('example.db')


    #delete_db_file('example.db')


if __name__ == '__main__':
    main()
