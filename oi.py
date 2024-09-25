import json

def count_telegram_user_ids(file_name):
    with open(file_name, 'r') as file:
        data = json.loads(file.read())  # Parse the JSON string
        telegram_user_ids = [int(user_id) for user_id in data.keys() if data[user_id] is None]
        return len(telegram_user_ids)

file_name = 'user_data.json'
telegram_count = count_telegram_user_ids(file_name)
print(f"The number of Telegram user IDs in {file_name} is: {telegram_count}")

