import pandas as pd
import numpy as np
from logging import getLogger


TRAIN_PRODUCTS = '~/input/cproducts.csv'
TRAIN_TENDER = '~/input/ctender.csv'
SUBMIT_FILE =  '~/input/sub1.csv'
logger = getLogger(__name__)


def read_products():
    logger.debug('enter')
    df = pd.read_csv(TRAIN_PRODUCTS)
    logger.debug('exit')
    return (df)
            
def read_tender():
    logger.debug('enter')
    df =  pd.read_csv(TRAIN_TENDER)
    logger.debug('exit')
    return (df)

def load_test_data():
    logger.debug('enter')
    df = pd.read_csv(SUBMIT_FILE)
    logger.debug('exit')
    return (df)

if __name__ == '__main__':
    print (load_test_data().head())
    print (read_tender().head())
                    
