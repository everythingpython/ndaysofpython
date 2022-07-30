from functools import wraps
from time import time
import os

def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        print(f'func:{f.__name__} took: {(te-ts):2.4f} sec\n')
        return result
    return wrap

def sqrt_num(n):
    """ Returns the sqrt of a number """
    return n, n**0.5
    
    
def get_file_size(filename):
    file_size = os.path.getsize(filename)
    file_size = file_size/(1024.0*1024.0)
    file_size = round(file_size,2)
    return file_size