import logging, logging.config

# set up logging
logging.config.fileConfig("logging.conf")
logger = logging.getLogger("sLogger")

# log something
logger.debug("debug message")
logger.info("info message")
logger.warning("warn message")
logger.error("error message")
logger.critical("critical message")


try:
    with open("lesson3-tuple.py", 'rb') as f:
        ...
    logger.info('File successfully read')
except Exception as e:
    logger.error('Failed to open: ' + str(e))