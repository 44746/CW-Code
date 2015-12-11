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
			 rating integer,
			 email text,
			 position text,
			 avaliable text,
			 
			 primary Key(PlayerID))"""
		self.execute_sql(sql)
		
		sql = """create table if not exists Match
			 (MatchID integer,
			 date text,
			 opposition text,
			 result text,
			 
			 primary Key(MatchID))"""
		self.execute_sql(sql)
		
		sql = """create table if not exists Goals
				(GoalID integer,
				MatchID integer,
				PlayerID integer,
				Quantity integer,
				
				primary Key(GoalID))"""
		self.execute_sql(sql)

	def execute_sql(self, sql):
		with sqlite3.connect(self._db_name) as db:
			cursor = db.cursor()
			cursor.execute(sql)
			db.commit()
	
	def GetAllMatches(self):
		with sqlite3.connect(self._db_name) as db:
			cursor = db.cursor()
			cursor.execute("select * from Match")
			Matches = cursor.fetchall()
			return Matches
	
	def GetAllPlayers(self):
		with sqlite3.connect(self._db_name) as db:
			cursor = db.cursor()
			cursor.execute("select * from Player")
			players = cursor.fetchall()
			return players
			
	def AddMatch(self,date,opposition, result):
		with sqlite3.connect(self._db_name) as db:
				cursor = db.cursor()
				sql = "insert into Match(date,opposition,result) values ((SELECT max(MatchID) FROM Match)+1,'{0}', '{1}', '{2}')".format(date,opposition,result)
				cursor.execute(sql)
				db.commit()
			

	def AddPlayer(self,forename, surname, rating, email, position, avaliable):
		
		with sqlite3.connect(self._db_name) as db:
			cursor = db.cursor()
			sql = "insert into Player(PlayerID,forename, surname, rating, email, position, avaliable) values ((SELECT max(PlayerID) FROM Player)+1,'{0}','{1}', {2}, '{3}', '{4}', '{5}')".format(forename, surname, rating, email, position, avaliable)
			print(sql)
			cursor.execute(sql)
			db.commit()
			
g_database = Database("Player_Database.db")
