import http.server
import socketserver
import webbrowser
import os
import sys

PORT = 8000
DIRECTORY = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'website')

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

def start_server():
    os.chdir(DIRECTORY)
    server = None
    port = PORT
    for attempt_port in [8000, 8080, 8888, 5000, 3000]:
        try:
            server = socketserver.TCPServer(("", attempt_port), Handler)
            port = attempt_port
            break
        except OSError:
            continue
            
    if not server:
        print("Error: Could not bind to any standard port. Please close running applications and retry.")
        return

    url = f"http://localhost:{port}/index.html"
    print("=" * 70)
    print("  SilkGuard: Biology for Engineers Mulberry Leaf Laboratory")
    print(f"  Live local server running at: {url}")
    print("=" * 70)
    print("  Press Ctrl+C to stop the server.")
    print("=" * 70)
    
    webbrowser.open(url)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down SilkGuard server.")
        server.server_close()

if __name__ == '__main__':
    start_server()
