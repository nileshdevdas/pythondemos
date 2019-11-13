import logging

# LEVEL = TRACE , DEBUG , INFO , WARN , ERROR
FORMAT = '%(asctime)s   %(levelname)s   %(funcName)s   %(message)s'

logging.basicConfig(level="DEBUG", filename="d:/myapp.log", format=FORMAT)

logging.info("Hello from nilesh")
logging.debug("XXXXXXXXXXXXXXXXXXXXXXXx")
logging.error("THis will print......")