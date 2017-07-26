import webbrowser


"""
Os Command
"""
# from os command
python -m webbrowser -t "http://www.python.org"
# options(-n: new window, -t: new tab)


"""
Script
"""
# display "url" using the default browser.
webbrowser.open(url, new=0, autoraise=True)
# new = {0: same window ,1: new window, 2: new tab}
# autoraise = {"True": display in front window}

# handle browser with this controller.
controller.open(url, new=0, autoraise = True)
