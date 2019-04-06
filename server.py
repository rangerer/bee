import json
from datetime import datetime
import ssl

import tornado.web
import tornado.websocket
import tornado.ioloop
import tornado.httpserver

transactions = []

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello World")


class OCPPHandler(tornado.websocket.WebSocketHandler):
    CALLRESULT = 3
    CALLERROR = 4
    def open(self):
        print("OCPP connection established")

    def on_message(self, message):
        print("OCPP message {} received".format(message))
        MessageTypeId, UniqueId, Action, Payload = json.loads(message)

        try:
            if Action == "BootNotification":
                response = {
                    "currentTime": datetime.now().isoformat(),
                    "interval": 300,
                    "status": "Accepted"
                }
            elif Action == "Authorize":
                response = {
                    "status": "Accepted"
                }
            elif Action == "StartTransaction":
                response = {
                    "idTagInfo": {
                        "status": "Accepted"
                    },
                    "transactionId": len(transactions)
                }
                transactions.append(Payload)
            elif Action == "StopTransaction":
                response = {}
                transactionsId = Payload["transactionId"]
                transaction = transactions[transactionsId]
                consumption = Payload["meterStop"] - transaction["meterStart"]
                price = consumption / 1000 * 0.2

                print("transaction {} consumed {} Wh for {} Euro".format(transactionsId, consumption, price))
            else:
                raise NotImplementedError
            
            self.write_message(json.dumps([
                self.CALLRESULT, UniqueId, response
            ]))
        except NotImplementedError:
            self.write_message(json.dumps([
                self.CALLERROR, UniqueId, "NotImplemented", "Action {} not implemented".format(Action)
            ]))
        
    def on_close(self):
        print("OCPP connection closed")


if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/", MainHandler),
        (r"/ocpp", OCPPHandler)
    ])
    sslcontext = ssl.create_default_context(purpose=ssl.Purpose.CLIENT_AUTH)
    sslcontext.load_cert_chain(certfile="server.crt", keyfile="server.key")
    sslcontext.load_verify_locations(cafile="client.crt")
    server = tornado.httpserver.HTTPServer(app, ssl_options=sslcontext)
    server.listen(4443)
    tornado.ioloop.IOLoop.current().start()