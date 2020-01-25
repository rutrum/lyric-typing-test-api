import mysql.connector
from mysql.connector import errorcode

print('ljksdfkj')

pass_file = open("root_pass.txt")
root_pass = pass_file.read().strip()

try:
    cnx = mysql.connector.connect(
        host='35.193.10.101',
        database='typingtest',
        user='root',
        password=root_pass
    )
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)


def add_new_score(name, geniusID, time, score, spotifyID):
    insert = cnx.cursor()
    query = "INSERT INTO entries (username, geniusID, milliseconds, time, spotifyID) VALUES (%s, %s, %s, %s, %s);"
    val = (name, int(geniusID), int(time), int(score), spotifyID)
    insert.execute(query, val)
    cnx.commit()

    print(insert.rowcount, "record inserted")
    #cnx.close()
    get_song_leaderBoard(geniusID, 10)


def get_song_leaderBoard(geniusID, listLength):
    get = cnx.cursor(dictionary=True)
    query = "SELECT * FROM entries WHERE geniusID = %s LIMIT %s;"
    val = (int(geniusID),listLength)
    get.execute(query, val)
    
    results = get.fetchall()

    for x in results:
        print(x)

def alter_table():
    alter = cnx.cursor()
    query = "ALTER TABLE entries CHANGE songID geniusID INT;"
    alter.execute(query)
    cnx.commit()
    cnx.close()

def get_all():
    get = cnx.cursor()
    query = "SELECT * FROM entries;"
    get.execute(query)

    print(get.fetchall())
    

def main():
    add_new_score('HandRob', '86916', '92393', '9344', '08dFHFTx6r67MTsYn5ilDR')
    #get_all()
    #alter_table()
    cnx.close()


if __name__ == "__main__":
    main()