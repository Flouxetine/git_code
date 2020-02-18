import logging
import os
import os.path as path
import time

# 第一步，创建一个logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# 第二步，创建一个handler，用于写入日志文件
log_date = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
# 工程目录下创建Logs文件夹
log_path = path.dirname(os.getcwd()) + '/Logs/'
log_name = log_path + log_date + '.log'
log_file = log_name
file_handler = logging.FileHandler(log_file,mode = 'w')
file_handler.setLevel(logging.DEBUG)

# 第三步，定义handler的输出格式
formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
file_handler.setFormatter(formatter)

# 第四步，将logger添加到handler里面
logger.addHandler(file_handler)

# 第五步，写入内容
logger.debug('this is a logger debug message')
logger.info('this is a logger info message')
logger.warning('this is a logger warning message')
logger.error('this is a logger error message')
logger.critical('this is a logger critical message')

