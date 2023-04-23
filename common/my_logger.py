import os
import sys

from loguru import logger

from common.config import VERSION


class MyLogger:
    def __init__(self, log_file_dir):
        # log_file_path = log_file_dir + datetime.datetime.now().strftime('%Y%m%d') + '.log'
        log_file_path = log_file_dir + 'v' + VERSION + '.log'
        self.logger = logger
        self.logger.remove()
        # 添加控制台输出的格式,sys.stdout为输出到屏幕;关于这些配置还需要自定义请移步官网查看相关参数说明
        self.logger.add(sys.stdout,
                        format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "  # 颜色>时间
                               "{process.name} | "  # 进程名
                               "{thread.name} | "  # 进程名
                               "<cyan>{module}</cyan>.<cyan>{function}</cyan>"  # 模块名.方法名
                               ":<cyan>{line}</cyan> | "  # 行号
                               "<level>{level}</level>: "  # 等级
                               "<level>{message}</level>",  # 日志内容
                        )
        # 输出到文件的格式
        self.logger.add(log_file_path, level='WARNING',
                        format='{time:YYYY-MM-DD HH:mm:ss} - '  # 时间
                               "{process.name} | "  # 进程名
                               "{thread.name} | "  # 进程名
                               '{module}.{function}:{line} - {level} -{message}',  # 模块名.方法名:行号
                        rotation="10 MB")

    def get_logger(self):
        return self.logger


# 设置日志
if not os.path.exists('logs'):
    os.mkdir('logs')
my_logger = MyLogger('logs/').get_logger()
