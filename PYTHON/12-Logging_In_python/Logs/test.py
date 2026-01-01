from logger import logging

def add(a,b):
    logging.debug(f'Addition operation is taking place')
    return a + b


logging.debug("This addition function is called")
add(10,15)