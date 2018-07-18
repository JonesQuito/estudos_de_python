import MySQLdb


def conectaDb(server, user, password, db):
    try:
        connection = MySQLdb.connect(server, user, password, db)
    except MySQLdb.Error as e:
        if e.args[0] == 1049:
            if(input('Base de dados inexistente. Deseja criar o banco : \' %s\'?' %db))== 's':
                connection = MySQLdb.connect(server, user, password)
                cursor = connection.cursor()
                cursor.execute('create database %s' %db)
                cursor.close()
                connection.close()
                return MySQLdb.connect(server, user, password, db)
            else:
                return 0
    return connection
                
