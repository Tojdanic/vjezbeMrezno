import SimpleHTTPServer
import SocketServer

PORT = 9000
Handler = SimpleHTTPServer.SimpleHTTPRequestHandler


httpd = SocketServer.TCPServer(("", PORT), Handler)


print "Working on port", PORT
httpd.serve_forever()