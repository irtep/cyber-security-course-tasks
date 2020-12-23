#!/usr/bin/env python3
import sys
import socket


def get_accessible_ports(address, min_port, max_port):
  found_ports = []
  #target = socket.gethostbyname(address)
  target = address
    # write code here
  try:

	    # will scan ports between 1 to 65,535
    for port in range(min_port,max_port+1):
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      #socket.setdefaulttimeout(1)

	        # returns an error indicator
      result = s.connect_ex((target,port))
      if result ==0:
        #print('found '+port)
        found_ports.append(port)
	        #    print("Port {} is open".format(port))
        s.close()
      #else:
    #    print('not ok: '+str(port))

  except KeyboardInterrupt:
     print("\n Exitting Program !!!!")
     sys.exit()
  except socket.gaierror:
     print("\n Hostname Could Not Be Resolved !!!!")
     sys.exit()
  except socket.error:
     print("\ Server not responding !!!!")
     sys.exit()
  return found_ports


def main(argv):
    address = sys.argv[1]
    min_port = int(sys.argv[2])
    max_port = int(sys.argv[3])
    ports = get_accessible_ports(address, min_port, max_port)
    for p in ports:
        print(p)

# This makes sure the main function is not called immediatedly
# when TMC imports this module
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print('usage: python %s address min_port max_port' % sys.argv[0])
    else:
        main(sys.argv)
