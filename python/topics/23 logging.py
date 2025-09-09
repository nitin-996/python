import logging

# Create a logger
logger = logging.getLogger("my_app")
logger.setLevel(logging.DEBUG)

# Console handler
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

# File handler
fh = logging.FileHandler("my_app.log")
fh.setLevel(logging.DEBUG)

# Formatter
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
ch.setFormatter(formatter)
fh.setFormatter(formatter)

# Add handlers to logger
logger.addHandler(ch)
logger.addHandler(fh)

# Usage
logger.debug("Debugging details")
logger.info("Starting application")
logger.warning("This is a warning")
logger.error("Error occurred")
logger.critical("Critical failure")
