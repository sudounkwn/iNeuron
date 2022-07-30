import logging

'''this is logger file thats logs all the events'''

try:
    logg=logging.getLogger(__name__)
    logg.setLevel(logging.INFO)
    logFileHand = logging.FileHandler('logger.log')
    logFormat = logging.Formatter("%(asctime)s|%(levelname)s|%(name)s|%(filename)s|%(message)s")
    logFileHand.setFormatter(logFormat)
    logg.addHandler(logFileHand)

except Exception as e:
    logg.info('Exception occured::',e)
