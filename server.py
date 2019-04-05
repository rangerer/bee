import tornado.web
import tornado.websocket
import tornado.ioloop


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello World")


class OCPPHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print("OCPP connection established")

    def on_message(self, message):
        print("OCPP message {} received".format(message))
    
    def on_close(self):
        print("OCPP connection closed")


if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/", MainHandler),
        (r"/ocpp", OCPPHandler)
    ])
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()