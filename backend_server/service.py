import operations
import pyjsonrpc

SERVER_HOST = 'localhost'
SERVER_PORT = 4040

class RequestHandler(pyjsonrpc.HttpRequestHandler):


    """ Get news summaries for a user """
    @pyjsonrpc.rpcmethod
    def getNewsSummariesForUser(self, user_id, page_num):
        return operations.getNewsSummariesForUser(user_id, page_num)

    """ Log user news clicks """
    @pyjsonrpc.rpcmethod
    def logNewsClickForUser(self, user_id, news_id):
        return operations.logNewsClickForUser(user_id, news_id)

    @pyjsonrpc.rpcmethod
    def searchNews(self, keyword, page_num):
        return operations.searchNews(keyword, page_num)
        

# Threading HTTP Server
http_server = pyjsonrpc.ThreadingHttpServer(
  server_address = (SERVER_HOST, SERVER_PORT),
  RequestHandlerClass = RequestHandler
)

print "Starting HTTP server on %s:%d" % (SERVER_HOST, SERVER_PORT)

http_server.serve_forever()
