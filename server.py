from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlsplit


class NoCacheHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        requested_url = urlsplit(self.path)
        is_page_request = requested_url.path in ("/", "/index.html")
        is_current_page = (
            requested_url.path == "/index.html"
            and requested_url.query == "clean=17"
        )

        if is_page_request and not is_current_page:
            self.send_response(302)
            self.send_header("Location", "/index.html?clean=17")
            self.end_headers()
            return
        super().do_GET()

    def end_headers(self):
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate, max-age=0")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        self.send_header("Clear-Site-Data", '"cache"')
        super().end_headers()


if __name__ == "__main__":
    server = ThreadingHTTPServer(("0.0.0.0", 5000), NoCacheHandler)
    print("Serving on http://0.0.0.0:5000 with caching disabled")
    server.serve_forever()