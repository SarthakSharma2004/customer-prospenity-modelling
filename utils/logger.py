import logging

logging.basicConfig(level = logging.INFO,
                    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                    datefmt = '%Y-%m-%d %H:%M:%S' , 
                    filename = 'app.log',
                    filemode = 'a'
)

def get_logger(name) :
    return logging.getLogger(name)