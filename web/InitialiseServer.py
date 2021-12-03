'''import http.server
import socketserver


class FilesHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    """This class is to use files as a stream of a server"""
    def do_GET(self):
        if self.path == '/':
            self.path = 'somewebpage.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)


def run_http_server(port):
    with socketserver.ThreadingTCPServer(("", port), FilesHttpRequestHandler) as httpd:
        try:
            print("serving at port", port)
            httpd.serve_forever()
        finally:
            print("closing the port", port)
            httpd.server_close()
'''