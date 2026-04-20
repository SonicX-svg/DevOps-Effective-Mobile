from http.server import HTTPServer, BaseHTTPRequestHandler
from socketserver import ThreadingMixIn
import os

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/nginx-python-health":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'OK')
            return
        self.send_response(200)
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()
        
        # Читаем переменные окружения
        app_name = os.getenv('APP_NAME', 'unknown')
        working_dir = os.getcwd()
        
        message = f"Hello from Effective Mobile!\n"
        
        self.wfile.write(message.encode())
    

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer): 
    pass

if __name__ == '__main__':
    port = int(os.getenv('BACKEND_PORT', 8000))
    server = ThreadedHTTPServer(('0.0.0.0', port), Handler)
    print(f'Backend running on port {port} with parallel threads')
    print(f'App name: {os.getenv("APP_NAME")}')
    server.serve_forever()
