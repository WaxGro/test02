import logging
class Log():
    def __init__(self,f):
        self.f=f
    def log(self):
        loger=logging.getLogger()
        loger.setLevel(1)
        f  = logging.Formatter(
            '%(name)s--%(levelname)s--%(funcName)s--%(asctime)s--%(message)s'
        )
        g = logging.FileHandler(
            self.f,mode='w',encoding='utf-8'
        )
        g.setFormatter(f)
        loger.addHandler(g)
