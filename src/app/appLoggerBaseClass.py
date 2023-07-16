import logging


def _setup():

    _logger = logging.getLogger("MongoDBQueryHelper")

    #_logger.setLevel(level=logging.INFO)
    _logger.setLevel(level=logging.DEBUG)
    #_logger.setLevel(level=logging.ERROR)
    #_logger.setLevel(level=logging.WARNING)

    _fileHandler = logging.FileHandler(
        filename="logs/log.txt",
        mode="a", 
    )

    
    _logger.addHandler(_fileHandler)

    return _logger

 

class AppLoggerBaseClass: 
    appLogger = _setup()


