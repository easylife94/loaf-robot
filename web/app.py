import tornado.ioloop
import tornado.web
import aiml
import os
from Robot import Robot



class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

class ChatHandler(tornado.web.RequestHandler):
    robot = Robot();

    def get(self):
        req = self.get_argument("req")
        self.write(self.robot.respond(req));
application = tornado.web.Application([
    (r"/",MainHandler),
    (r"/chat",ChatHandler)
])

if __name__=="__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
