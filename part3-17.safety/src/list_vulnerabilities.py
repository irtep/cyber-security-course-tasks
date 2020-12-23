#!/usr/bin/env python3
import sys
import json


def get_vulnerabilities(name, db):
	vulnes = []
	fixedVulnes = []
	theList = json.load(db)
#	print(theList)
	for pack in theList:
		if name == pack:
			insides = theList[pack]
			for ins in insides:
				for ii in ins:
					dublicated = False
					newEntry = (ins['id'], ins['v'], ins['cve'])
					for ee in vulnes:
						if ee == newEntry:
							dublicated = True
					if dublicated == False:
						vulnes.append(newEntry)
#					if ins == 'id':
#						idn = ins[ii]

#					if ins == 'v':
#						ver = ins[ii]
#					if ins == 'cve':
#						cve = ins[ii]
#					if idn != 'null' and ver != 'null' and cve != 'null':
#						newEntry = (idn, ver, cve)
#						print('new entry: ', newEntry)
#						vulnes.append(newEntry)
#						idn = 'null'
#						ver = 'null'
#						cve = 'null'
# zwiki 1, ampache 3
			#jsoned = json.dumps(insides)
			#jsoned2 = json.dumps(jsoned)
			#print(jsoned2)
#			for entr in insides:
#				entry = insides[entr]
#				vulnes.append(entry)
		#vulnes.append(pack)
		#print((pack, '->', theList[pack]))
	#with open(db) as f:
#		data = json.load(f.read())
    	#print(data[0]['text'])
#		vulnes.append(data)
	#print('vules: ', vulnes)
#	print(type(vulnes[0]))
	#for pack in theList:
	#	if name = pack
	return vulnes


def main(argv):
	name = sys.argv[1]
	db = open(sys.argv[2])
	vulnerabilities = get_vulnerabilities(name, db)
	for v in vulnerabilities:
		print('%s; %s; %s' % (v[0], v[1], v[2]))


# This makes sure the main function is not called immediatedly
# when TMC imports this module
if __name__ == "__main__":
	if len(sys.argv) != 3:
		print('usage: python %s name db' % sys.argv[0])
	else:
		main(sys.argv)
