# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer
import os
import logging

# class SecreteManager(object):
#     """Singleton class for managing secret

#     """
    
#     def __init__(self) -> None:
#         self.secret = None # Store the secret in memory
    
#     def set_secret(self, secret:str):
#         """Setter for secret         

#         Args:
#             secret (str): the string value of secret
#         """
#         self.secret = secret
    
#     def get_secret(self):
#         """Getter for secret

#         Returns:
#             string: the secret value
#         """
#         if not self.secret:
#             logging.error("Secret is not set")
#         else:
#             return self.secret
        
#     def __new__(cls):
#         """Singleton get or create

#         Returns:
#             SecreteManager: instance of SecreteManagers
#         """
#         if not hasattr(cls, 'instance'):
#             cls.instance = super(SecreteManager, cls).__new__(cls)
#         return cls.instance
secret = None
class CdcHttpRequestHandler(BaseHTTPRequestHandler):

    def get_secret_length(self):
        """To get the length of secret

        Returns:
            int: the value of secret length
        """
        return len(secret)
    
    def do_GET(self):
        # TODO: Path routing
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(f"it is of {self.get_secret_length()} length", "utf-8"))

if __name__ == "__main__":

    # Env 
    url = os.getenv("CDC_HTTP_BASE_URL", "localhost")
    httpPort = os.getenv("CDC_HTTP_LISTEN_PORT", 18080)
    httpListenAddress = os.getenv("CDC_HTTP_LISTEN_ADDRESS", "127.0.0.1")
    logLevel = os.getenv("CDC_LOG_LEVEL", "INFO")
    secret = os.getenv("CDC_SECRET_VALUE", "123") # TODO will read from somewhere else
    
    # Config logger
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.getLevelName(logLevel))
    
    webServer = HTTPServer((httpListenAddress, httpPort), CdcHttpRequestHandler)
    logging.info("Server started http://%s:%s" % (httpListenAddress, httpPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    logging.info("Server stopped.")