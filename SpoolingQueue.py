from multiprocessing import get_context
import multiprocessing.queues as mpq
import multiprocessing.connection as connection

class SpoolingQueue(mpq.Queue):

    def __init__(self,*args,**kwargs):
        ctx = get_context()
        super(SpoolingQueue, self).__init__(*args, **kwargs, ctx=ctx)

    def wait(self):
        connection.wait([self._reader])