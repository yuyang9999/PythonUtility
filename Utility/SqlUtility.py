import MySQLdb

class MySQLConn:
	def __init__(self,host,db_name,user_name,password):
		conn=MySQLdb.connect(host=host,user=user_name,passwd=password,db=db_name)
		conn.set_character_set('utf8')

		cursor=conn.cursor()

		cursor.execute('SETNAMESutf8;')
		cursor.execute('SETCHARACTERSETutf8;')
		cursor.execute('SETcharacter_set_connection=utf8;')

		self.conn=conn
		self.cursor=cursor