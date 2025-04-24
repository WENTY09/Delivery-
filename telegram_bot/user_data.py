import os
import json
from datetime import datetime, timedelta

DATA_FILE = "data/user_data.json"

def _load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return {}

def _save_data(data):
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)

def get_user_data(user_id):
    data = _load_data()
    user_id_str = str(user_id)
    if user_id_str not in data:
        data[user_id_str] = {
            "deliveries": 0,
            "money": 0,
            "last_delivery": None,
            "buffs": []
        }
    return data[user_id_str]

def update_user_data(user_id, deliveries, earnings):
    data = _load_data()
    user_id_str = str(user_id)
    user = get_user_data(user_id)
    multiplier = get_active_earnings_multiplier(user_id)
    buffed_earnings = int(earnings * (1 + multiplier))
    user["deliveries"] += deliveries
    user["money"] += buffed_earnings
    user["last_delivery"] = datetime.now().isoformat()
    data[user_id_str] = user
    _save_data(data)
    return earnings, buffed_earnings

def can_deliver(user_id):
    user = get_user_data(user_id)
    if not user["last_delivery"]:
        return True, 0
    last = datetime.fromisoformat(user["last_delivery"])
    now = datetime.now()
    if now - last >= timedelta(seconds=30):
        return True, 0
    remaining = 30 - (now - last).seconds
    return False, remaining

def get_active_earnings_multiplier(user_id):
    user = get_user_data(user_id)
    now = datetime.now()
    active_buffs = [b for b in user["buffs"] if datetime.fromisoformat(b["expires_at"]) > now]
    total_multiplier = sum(buff["bonus"] for buff in active_buffs)
    user["buffs"] = active_buffs
    _save_data(_load_data())
    return total_multiplier
