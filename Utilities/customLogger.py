import logging
import time
# from logging.handlers import TimedRotatingFileHandler
class LogGen:
    @staticmethod
    def loggen(name):
        # h = TimedRotatingFileHandler("C:/Users/Goodwin/Documents/FaceBookApp/Logs/logger.log")
        # logging.basicConfig(filename=h,filemode= "w",format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',force= True)
        # logger=logging.getLogger()
        # logger.root.setLevel(logging.INFO)
        # print("----------",logger)
        # return logger
        logger = logging.getLogger(name)
        log_folder = f'.\\Logs\\automation_{time.strftime("%Y-%m-%d %H_%M_%S", time.gmtime()).split()[1]}.log'
        fhandler = logging.FileHandler(filename=log_folder, mode='a')
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fhandler.setFormatter(formatter)
        logger.addHandler(fhandler)
        logger.setLevel(logging.INFO)
        return logger    
        
        
        
        
        # FORMAT = '%(asctime)s %(user)-8s %(message)s'
        # logging.basicConfig(format=FORMAT)
        # logging.basicConfig(filename="r.txt",filemode="w")
        # logger =logging.getLogger(__name__)
        # logger.setLevel(logging.INFO)
        # print("-----------",logger.info("starting"))
        # consoleHandler = logging.StreamHandler()
        # logger.addHandler(consoleHandler)
        # logFormatter = logging.Formatter("%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s")

    #     logging.basicConfig(
    #     level=logging.INFO,
    #     format="%(asctime)s [%(levelname)s] %(message)s",
    #     handlers=[
    #         logging.FileHandler("debug.log"),
    #         logging.StreamHandler()
    #     ]
    # )
    #     return logging