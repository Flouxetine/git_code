import logging
import error_output
import warning_output

def writeCritical():
    logging.critical(u"记录文件main.py的日志")

warning_output.wirteWarning()
error_output.writeError()
writeCritical()
