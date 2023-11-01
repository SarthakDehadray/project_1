from Insurance.logger import logging 
from Insurance.exception import InsuranceException
import os,sys

def test():
    try:
        logging.info("Starting the test logger function")
        result = 3/0
        print(result)
        logging.info("ending point of try")
    except Exception as e:
        logging.debug(str(e))
        raise InsuranceException(e,sys)

if __name__ == "__main__":
    try:
        test()
    except Exception as e:
        print(e)