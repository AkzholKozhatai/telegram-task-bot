from datetime import datetime

def get_current_datetime():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def is_admin(user_id: int, admin_ids: list[int]) -> bool:
    return user_id in admin_ids

