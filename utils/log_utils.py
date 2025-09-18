# utils/logger.py
import logging
import os

def setup_logger(name, log_file, level=logging.INFO):
    """Set up a logger with a specific name and log file"""
    os.makedirs('logs', exist_ok=True)
    
    logger = logging.getLogger(name)
    logger.setLevel(level)
    
    if logger.handlers:
        return logger

    file_handler = logging.FileHandler(log_file,mode='w')
    file_handler.setLevel(level)
    
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    
    return logger



# Convenience functions
def get_ingestion_logger():
    return setup_logger('ingestion', 'logs/ingestion_db.log')

def get_vendor_summary_logger():
    return setup_logger('vendor_summary', 'logs/vendor_summary.log')
def get_main_logger():
    return setup_logger('main', 'logs/main.log')