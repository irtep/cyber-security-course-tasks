#!/usr/bin/env python3
import sys
import sqlite3


def read_database(conn):
	agents = []

	# output should be a list of pairs
	# agents = [(id1, name1), (id2, name2), (id3, name3), ...] ordered by id
# conn = sqlite3.connect('mysqlite.db')
	cursor = conn.cursor()
	cursor.execute("SELECT A.id, A.name FROM Agent A ORDER BY A.id;")
	return cursor.fetchall()
	#c = conn.cursor()
	#c.execute('''SELECT id,name FROM agent;''')
	#rows1 = c.fetchall()
	#c.execute('''SELECT name FROM agent;''')
	#rows2 = c.fetchall()
	#print('r1 ', rows1)
	#c.execute('''SELECT id, name FROM agent;''')
	#rows = c.fetchall()
	#rows3.sort()
	#print('r2', rows2)
	#print('r3 ', rows3)
	#for x in rows1:
		#print('x: ', x)
		#print('val: ', val)
		#print('rows2[val] ', rows2[val])
		#addOn = x + rows2[val]
	#	agents.append(x)
	#agents = rows
#commit the changes to db
	#conn.commit()
#close the connection
	#conn.close()
	#agents = rows
	#print('printing: ', agents)
	#return agents



def main(argv):
	name = sys.argv[1]
	conn = sqlite3.connect(name)
	agents = read_database(conn)
	for agent in agents:
		print(agent[0], agent[1])

# This makes sure the main function is not called immediatedly
# when TMC imports this module
if __name__ == "__main__":
	if len(sys.argv) != 2:
		print('usage: python %s database' % sys.argv[0])
	else:
		main(sys.argv)
