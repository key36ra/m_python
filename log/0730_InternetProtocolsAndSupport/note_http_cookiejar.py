import http.cookiejar

"""
Overview
"""
# "http.cookiejar" module  is class of processing HTTP Cookie automatically.

# Create 
class http.cookiejar.CookieJar(plicy=None)


"""
Example
"""
# Ex1."The most common usage of http.cookiejar."
import http.cookiejar, urllib.request
cj = http.cookiejar.CookieJar()
opener = urllib,request.build_opener(urllib.request.HTTPCookieProcessor(cj))

# Ex2."Use Netscape, Mozilla or Lynx Cookie when open URL."
import os, http.cookiejar, urllib.request
cj = http.cookiejar.MozillaCookieJar()
cj.load(os.path.join(os.path.expanduser("~"),".netscape","cookies.txt"))
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
r = opener.open("http://example.com/")

# Ex3."Usage of DefaultCookiePolicy."
import urllib.request
from http.cookiejar import CookieJar, DefaultCookiePolicy
policy = DefaultCookiePolicy(
    rfc2965=True, strict_ns_domain=Policy.DomainStrict,
    blocked_domains=["abs.net",".ads.net"])
cj = CookieJar(policy)
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
r = opener.open("http://example.com/")
