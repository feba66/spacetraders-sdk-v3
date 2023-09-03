from spacetraders_sdk.spacetraders_logger import SpaceTradersLogger
logger = None

def test_init():
    global logger
    logger = SpaceTradersLogger("test-logger")
    
    assert logger != None

def test_logging():
    global logger
    logger.debug("Debug Log")
    logger.info("Info Log")
    logger.warn("test warning%s","!")
    logger.error("test error%s","!")
    logger.fatal("test fatal%s","!")