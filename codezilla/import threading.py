import time 
from threading import Thread

def do_this():
    print('starting this!')
    # Simulate doing this
    time.sleep(2)
    print('Did this!')
    
def do_that():
    print('starting that!')
    # Simulate doing that
    time.sleep(3)
    print('Did that!')
    
t1 = Thread(target=do_this)
t1.start()
    
t2 = Thread(target=do_that)
t2.start()