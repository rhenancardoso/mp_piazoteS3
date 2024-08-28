import socket


class WebServer:
    def __init__(self) -> None:
        self.web_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.web_socket.bind(("", 80))
        self.web_socket.listen(5)
        self.web_socket.setblocking(False)

    def _web_page(self):
        """Retrieve HTML webpage."""
        from .web_page import WEB_PAGE_HTML  # avoid cyle-import

        return WEB_PAGE_HTML

    def check_request(self) -> bool:
        """Listen to request and reply with the webpage to the websocket."""
        try:
            conn, addr = self.web_socket.accept()
            print("Got a connection from %s" % str(addr))
            request = conn.recv(1024)
            print("Content = %s" % str(request))
            response = self._web_page()
            conn.send(response)
            conn.close()
            return True
        except OSError:
            return False
