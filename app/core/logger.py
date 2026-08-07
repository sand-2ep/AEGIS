import logging

def create_formatter():
    return logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

def create_console_handler(formatter):
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    return handler

def create_logger():
    logger = logging.getLogger("AEGIS")
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        formatter = create_formatter()
        handler = create_console_handler(formatter)
        logger.addHandler(handler)

    logger.propagate = False
    return logger

logger = create_logger()