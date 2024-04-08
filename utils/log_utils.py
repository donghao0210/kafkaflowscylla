import logging

# Create a logger object
logger = logging.getLogger(__name__)
insertion_logger = logging.getLogger('insertion')

# Set the log level to DEBUG so all log messages are recorded
logger.setLevel(logging.DEBUG)
insertion_logger.setLevel(logging.DEBUG)

# Create file handlers for outputting log messages to different files
info_handler = logging.FileHandler('logs/info.log')
insertion_handler = logging.FileHandler('logs/insertion.log')
warning_handler = logging.FileHandler('logs/warning.log')
error_handler = logging.FileHandler('logs/error.log')

# Set the log level for each handler
info_handler.setLevel(logging.INFO)
insertion_logger.setLevel(logging.INFO)
warning_handler.setLevel(logging.WARNING)
error_handler.setLevel(logging.ERROR)

# Create a formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
info_handler.setFormatter(formatter)
insertion_handler.setFormatter(formatter)
warning_handler.setFormatter(formatter)
error_handler.setFormatter(formatter)

# Add the handlers to the logger
logger.addHandler(info_handler)
insertion_logger.addHandler(insertion_handler)
logger.addHandler(warning_handler)
logger.addHandler(error_handler)