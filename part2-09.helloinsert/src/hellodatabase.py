#!/usr/bin/env python3
import sys
import sqlite3


def add_agent(conn, aid, name):
	data = (aid, name)
	cursor = conn.cursor()
	cursor.execute("INSERT INTO Agent VALUES (?, ?)", data)
	conn.commit()

def delete_agent(conn, aid):
	data = (aid, )
	cursor = conn.cursor()
	cursor.execute("DELETE FROM Agent WHERE id = ?", data )
	conn.commit()

def read_database(conn):
	agents = []
	cursor = conn.cursor()
	for a in cursor.execute("SELECT A.id, A.name FROM Agent A ORDER BY A.id;"):
		agents.append(a)
	return agents

def main(argv):
	name = sys.argv[1]
	conn = sqlite3.connect(name)
	while True:
		agents = read_database(conn)
		print('\nActive agents:\n')
		for agent in agents:
			print(agent[0], agent[1])
		print()
		command = input('What would you like to do: [a]dd, [r]emove, or [q]uit? ')

		if command[0].startswith('a'):
			aid = input('id? ')
			name = input('name? ')
			add_agent(conn, aid, name)
			pass
		elif command[0].startswith('r'):
			aid = input('id? ')
			delete_agent(conn, aid)
			pass
		elif command[0].startswith('q'):
			break


# This makes sure the main function is not called immediatedly
# when TMC imports this module
if __name__ == "__main__":
	if len(sys.argv) != 2:
		print('usage: python %s database' % sys.argv[0])
	else:
		main(sys.argv)
