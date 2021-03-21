import logging



class LogGen:
    @staticmethod
    def loggen():
        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)

            logging.basicConfig(filename="./Logs/automation.log", filemode='w',
                        format='%(asctime)s: %(levelname)s: %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p')
            logger = logging.getLogger()
            logger.setLevel(logging.INFO)
            return logger

#class LogGen:
#    @staticmethod
 #   def loggen():
  #      logging.basicConfig(filename=".\\Logs\\automation.log",filemode='w',format='%(asctime)s: %(levelname)s:',datefmt= '%m/%d/%Y %I:%M:%S %p')
   #     logger = logging.getLogger()
    #    logger.setLevel(logging.INFO)
     #   return logger

