from functools import wraps
from time import time

def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        print(f'func:{f.__name__} args:[{args}, {kw}] took: {(te-ts):2.4f} sec\n')
        return result
    return wrap

def sqrt_num(n):
    """ Returns the sqrt of a number """
    return n, n**0.5
    
    