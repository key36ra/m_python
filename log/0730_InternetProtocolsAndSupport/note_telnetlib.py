import telnetlib

"""
Overview
"""
# "Telnet" class is connection to Telnet server.
class telnetlib.Telnet(host=None,port=0[,timeout])
# this is only socket.
# you must use "open()" method to connect actually.

# A "Telnet" object is a context manager and can be used in a "with" state.
# When the "with" block ends, the "close()" method is called.
from telentlib import Telnet
with Telnet('localhost',23) as tn:
    tn.interact()


"""
Method of "Telnet Object"
"""
# Read byte until read "expected" string, or cost "timeout" time.
Telnet.read_until(expected,timeout=None)
# Nealy "read_all()" method read all byte.

# Connect to server host.
Telnet.open(host,port=0[,timeout])

# Write byte to socket.
Telnet.write(buffer)

# Emurate low telnet client
Telnet.interact()



"""
Telnet Example
"""
import getpass
import telnetlib
 
# Input HOST, user, and password().
HOST = "localhost"
user = input("Enter your remote account:")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"login:")
tn.write(user.encode('ascii')+b"\n")
if password:
    tn.read_until(b"Password:")
    tn.write(password.encode('ascii')+b"\n")

tn.write(b"Is\n")
tn.write(b"exit\n")

print(tn.read_all().decode("ancii"))