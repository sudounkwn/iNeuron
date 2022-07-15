import logging
'''This is logger file implementation for Rajashekhargoud_Assignment_9th_July package '''
try:
    logg = logging.getLogger(__name__)
    logg.setLevel(logging.INFO)
    fil = logging.FileHandler('logsForAssignment.log')
    loggFormat = logging.Formatter("%(asctime)s|%(levelname)s|%(name)s|%(filename)s|%(message)s")
    fil.setFormatter(loggFormat)
    logg.addHandler(fil)
except Exception as e:
    print('Exception occured ',e)

