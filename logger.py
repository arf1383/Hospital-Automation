import logging

def setup_logger():
    """تنظیمات اولیه برای لاگینگ"""
    logging.basicConfig(filename="hospital.log", level=logging.INFO,
                        format="%(asctime)s - %(levelname)s - %(message)s")

def log_event(message):
    """لاگ‌کردن رویدادها"""
    logging.info(message)
