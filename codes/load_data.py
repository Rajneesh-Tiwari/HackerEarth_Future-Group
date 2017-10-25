import pandas as pd
import numpy as np
from logging import getLogger

products = '../input/cproducts.csv'
tender = '../input/ctender.csv'
submission1 = '../input/sub1.csv'
submission2 = '../input/sub2.txt'

logger = getLogger(__name__)


def read_products():
    logger.debug('Start')
    df = pd.read_csv(products)
    logger.debug('Exit')
    return df


def read_tender():
    logger.debug('Start')
    df = pd.read_csv(tender)
    logger.debug('Exit')
    return df

def read_submission1():
    logger.debug('Start')
    df = pd.read_csv(submission1)
    logger.debug('Exit')
    return df

def read_submission2():
    logger.debug('Start')
    df  = pd.read_csv(submission2)
    logger.debug('Exit')
    return df


if __name__ == "__main__":
    print ("----------------------")
    print(read_products().head())
    print ("----------------------")
    print(read_tender().head())
    print ("----------------------")
    print (read_submission1().head())
    print ("----------------------")
    print (read_submission2().head())

    
