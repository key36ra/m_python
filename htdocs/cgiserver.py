from http import server
address = ("", 8000)
handler = server.CGIHTTPRequestHandler
server = server.HTTPServer(address, handler)
server.serve_forever()

