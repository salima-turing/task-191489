import http.server
import socketserver

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
	print(f"SaaS Logging Server running on port {PORT}...")
	httpd.serve_forever()
