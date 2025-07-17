#!/usr/bin/env python3
import os
import logging
import sys

def setup_logger(name, log_level=logging.DEBUG):
    """
    设置并返回一个配置好的日志记录器
    
    参数:
        name: 日志记录器名称
        log_level: 日志级别 (默认为 DEBUG)
    
    返回:
        配置好的日志记录器
    """
    log_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'logs')
    os.makedirs(log_dir, exist_ok=True)
    
    log_file = os.path.join(log_dir, f'{name}.log')
    
    logger = logging.getLogger(name)
    logger.setLevel(log_level)
    
    if logger.handlers:
        logger.handlers.clear()
    
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(log_level)
    
    console_handler = logging.StreamHandler(sys.stderr)
    console_handler.setLevel(log_level)
    
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger

def get_logger(name):
    """
    获取一个已配置的日志记录器，如果不存在则创建一个
    
    参数:
        name: 日志记录器名称
    
    返回:
        配置好的日志记录器
    """
    logger = logging.getLogger(name)
    
    if logger.handlers:
        return logger
    
    return setup_logger(name)