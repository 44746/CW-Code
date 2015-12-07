import sqlite3

class Database:
    def __init__(self,db_name):
        self._db_name=db_name

    def CreateDatabase():
        db_name= "Player.db"
        sql = """create table if not exists Player
             (PlayerID integer,
             forename text,
             primary Key(PlayerID))"""
        execute_sql(db_name, sql)

    def execute_sql(db_name, sql):
        with sqlite3.connect(db_name) as db:
            cursor = db.cursor()
            cursor.execute(sql)
            db.commit()

    def GetAllPlayers(self):
        with sqlite3.connect(self._db_name)
            cursor = db.cursor
            cursor.execute("select * from Player")
            players = cursor.fetchall()
            return players

	def AddPlayer(forename):
		forename = self.AddPlayerGUI.forename.text()
		with sqlite3.connect(Player.db) as db:
			cursor = db.cursor()
			sql = "insert into player(forename) values ({0})".format(forename)
			cursor.execute(sql)
			db.commit()
	
	self.AddPlayerGUI.btnAdd_pushed.connect(self.AddPlayer)
		
		
		
g_database = Database("Player_Database")
