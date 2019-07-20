import logging
import sys


logger = logging.getLogger('client.main')
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(module)s - %(message)s')

file_handler = logging.FileHandler('client_main.log', encoding='utf-8')
file_handler.setLevel(logging.DEBUG)
stream_handler = logging.StreamHandler(sys.stderr)
stream_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)
# stream_handler.setFormatter(formatter)

logger.setLevel(logging.DEBUG)
logger.addHandler(file_handler)
logger.addHandler(stream_handler)
