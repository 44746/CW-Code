import sqlite3

class Database:
	def __init__(self,db_name):
		self._db_name=db_name
		self.CreateDatabase()

	def CreateDatabase(self):
		sql = """create table if not exists Player
			 (PlayerID integer,
			 forename text,
			 surname text,
			 rating text,
			 email text,
			 position text,
			 avaliable text,
			 
			 primary Key(PlayerID))"""
		self.execute_sql(sql)

	def execute_sql(self, sql):
		with sqlite3.connect(self._db_name) as db:
			cursor = db.cursor()
			cursor.execute(sql)
			db.commit()

	def GetAllPlayers(self):
		with sqlite3.connect(self._db_name) as db:
			cursor = db.cursor()
			cursor.execute("select * from Player")
			players = cursor.fetchall()
			return players

	def AddPlayer(self,forename, surname, rating, email, position, avaliable):
		with sqlite3.connect(self._db_name) as db:
			cursor = db.cursor()
			sql = "insert into player(forename, surname, rating, email, position, avaliable) values ('{0}')".format(forename, surname, rating, email, position, avaliable)
			cursor.execute(sql)
			db.commit()
			
g_database = Database("Player_Database.db")
