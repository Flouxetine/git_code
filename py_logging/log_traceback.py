import logging
import os.path
import os
import time


# 创建logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# 创建handler
# 文件的名字
log_date = time.strftime('%Y%m%d%H%M',time.localtime(time.time()))
log_path = os.path.dirname(os.getcwd()) + '/Logs/'
log_name = log_path + log_date + '.log'
log_file = log_name

file_handler = logging.FileHandler(log_file,mode='w')
file_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

try:
    open('/path/to/does/not/exist', 'rb')
except (SystemExit, KeyboardInterrupt):
    raise
except Exception as e:
    logger.error('Failed to open file', exc_info=True)