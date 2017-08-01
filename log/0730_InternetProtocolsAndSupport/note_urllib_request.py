import urllib.request


"""
Overview
"""
# Simple urlopen method.
urllib.request.urlopen(url)
# "url" is "URL name" or "Request Object".


"""
For Example
"""
# Ex1.'Input the data to CGI.'
req = urllib.request.Request(url="https://localhost/cgi-bin/test.cgi",
                             data=b"This data is passed to stbin of the CGI")
with urlliib.request.urlopen(req) as f:
    print(f.read().decode("utf-8"))
# Output:'Got Data:"This data is passed to stbin of the CGI".'

# Ex2."HTTP Basic Authentification."
# Create an OpenerDirector with support for Basic HTTP Authentication...
auth_handler = urllib.request.HTTPBasicAuthHandler()
auth_handler.add_password(realm='PDQ Application',
                          uri='https://mahler:8092/site-updates.py',
                          user='klem',
                          passwd='kadidd!ehopper')
opener = urllib.request.build_opener(auth_handler)
# ...and install it globally so it can be used with urlopen.
urllib.request.install_opener(opener)
urllib.request.urlopen('http://www.example.com/login.html')

# Ex3."Proxy Basic Authentification."
proxy_handler = urllib.request.ProxyHandler({'http': 'http://www.example.com:3128/'})
proxy_auth_handler = urllib.request.ProxyBasicAuthHandler()
proxy_auth_handler.add_password('realm', 'host', 'username', 'password')
opener = urllib.request.build_opener(proxy_handler, proxy_auth_handler)
# This time, rather than install the OpenerDirector, we use it directly:
opener.open('http://www.example.com/login.html')


# Ex4."Use Proxy."
proxies = {'http':'http://proxy.example.com:8080/'}
opener = urllb.request.FancyURLopener(proxies)
with opener.open("http://www.python.org") as f:
    f.read().decode('utf-8')


"""
Request class
"""
# return Request instance for "url".
class urllib.request.Request(url,data=None,headers={},origin_req_host=None,
                             unverifiable=False,method=None)
# "data" must be an object specifying additional data to send to
#the server, or None if no such data is needed.
# headers must be dictionary.

# "override" for own purpose is powerful method of urllib class.


"""
Request object
"""
# original url
Request.full

# URI scheme
Request.type

# URI authority. (host:port)
Request.host

# original host name.
Request.origin_req_host

# Request entity body.
Request.data


"""
OpenerDirector Object
"""
# open URL
OpenerDirector.open(url,data=None[,timeout])


"""
BaseHandler Object
"""



"""
HTTPHandler Object
"""
# send HTTP request(GET or POST ...) by "req.has_data()".
HTTPHandler.http_open(req)

# "HTTPSHandler" is same.


"""
FileHandler Object
"""
# if no host, this open the file in the "localhost".
FileHandler.file_open(req)