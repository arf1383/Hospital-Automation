import os

def clear_screen():
    """پاک‌سازی صفحه نمایش"""
    os.system("cls" if os.name == "nt" else "clear")
