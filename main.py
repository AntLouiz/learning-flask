import psycopg2
from settings import (
    DB_NAME,
    DB_PASSWORD,
    HOST,
    USER
)


def create_db():
    connection = psycopg2.connect(
        'dbname={} password={} host={} user={}'.format(
            DB_NAME,
            DB_PASSWORD,
            HOST,
            USER
        )
    )

    return connection


def create_table_cities(connection, cursor):
    try:
        cursor.execute('select * from cities')
        cursor.fetchall()
    except:
        cursor.execute("""
            create table cities (
                id serial primary key,
                city varchar(50),
                uf varchar(50)
            );
        """)
        connection.commit()

    return connection


def close(cursor, connection):
    cursor.close()
    connection.close()

    return True


def main():

    connection = create_db()
    cursor = connection.cursor()

    create_table_cities(connection, cursor)

    cursor.execute("""
        insert into cities (city, uf) values ('Parnaíba', 'PI');
        insert into cities (city, uf) values ('Teresina', 'PI');
    """)
    connection.commit()

    cursor.execute('select * from cities')
    data = cursor.fetchall()


    print(data)
    close(cursor, connection)


if __name__ == '__main__':
    main()
