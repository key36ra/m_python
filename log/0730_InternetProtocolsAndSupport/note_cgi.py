import cgi


"""
First of all
"""
# Header section
print("Content-Type: text/html") # HTML is following
print()             # blank line, end of headers

# Second section
print("<TITLE>CGI script output</TITLE>")
print("<H1>This is my first CGI script</H1>")
print("Hello, world!")


"""
cgi module
"""
# Debug to browser
import cgitb
cgitb.enable()

# Debug to file
import cgitb
cgitb.enable(display=0,logdir="/path/to/logdir")

# Investigate "name" and "addr" in form.
form = cgi.FieldStorage()       # create query name "dictionary",form.
if "name" not in form or "addr" not in form:
    print("<H1>Error</H1>")
    print("Please fill in the name and addr fields.")
    return
print("<p>name:",form["name"].value)
print("<p>addr:",form["addr"].value)

# Return "username" list.
value = form.getlist("username")
usernames = ",".join(value)

# Read upload file.
fileitem = form["userfile"]
if fileitem.file:
    # It's an uploaded file; count lines.
    linecount = 0
    while True:
        line = fileitem.file.readline()
        if not line: break
        linecount = linecount + 1


"""
Install CGI script
"""
# first of the script for interpreter
#!/usr/local/bin/python



"""
Debug CGI script
"""
# Call "test()" method of cgi module
cgi.test()

# Give query value to script from browser.
http://yourhostname/cgi-bin/cgi.py?name=Joe+Blow&addr=At+Home

# Browser debug
import cgitb
cgitb.enable()
