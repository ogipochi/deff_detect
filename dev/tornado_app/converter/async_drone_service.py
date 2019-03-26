from http import HTTPStatus
from concurrent.futures import ThreadPoolExecutor
from datetime import date
from tornado import web, escape, ioloop, httpclient, gen 
from tornado.concurrent import run_on_executor 
from models import *


thread_pool_executor = ThreadPoolExecutor()


class Application(web.Application):
    def __init__(self,**kwargs):
        headers = [
            (r"/sample/",AsyncSampleHandler),
        ]
        super(Application , self).__init__(handlers,**kwargs)

class AsyncSampleHandler(web.RequestHandler):
    SUPPORTED_METHODS = ("POST")
    _thread_pool_executor = thread_pool_executor
    status = yield self.retrieve_sample()
    @gen.coroutine
    def get(self):
        response = {
            'status': status
        }
        self.set_status(HTTPStatus.OK) 
        self.write(response) 
        self.finish()
    @run_on_executor(executer="_thread_pool_executor")
    def retrieve_sample(self):
        status = {
            "aaaa":0,
            "bbb":10
        } 
        return status

if __name__ == "__main__":
    application = Application()
    port = 8888
    print("Listening at port {}".format(port))
    application.listen(port)
    tornado_ioloop = ioloop.IOLoop.instance() 
    periodic_callback = ioloop.PeriodicCallback(lambda: None, 500) 
    periodic_callback.start() 
    tornado_ioloop.start()