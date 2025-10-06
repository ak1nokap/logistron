import asyncio
import random
from telethon import TelegramClient

# ⚡ Данные API (получить на https://my.telegram.org)
api_id = 23506845
api_hash = "a015ff48c31ca309a5ef6543f8fe65dd"

# Создаём клиент
client = TelegramClient("session_name", api_id, api_hash)
symbols ='йцукенгшщзхъфывапролджэячсмитьбюЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ'


random_hash = "".join(random.choice(symbols) for _ in range(8))


async def main():
    # Читаем сообщение из файла
    with open("message.txt", "r", encoding="utf-8") as f:
        message_text = f.read().strip()
        final_text =random_hash+"\n"+message_text

    # Читаем список групп из файла
    with open("groups.txt", "r", encoding="utf-8") as f:
        groups = [line.strip() for line in f if line.strip()]

    print(f"📢 Найдено {len(groups)} групп для рассылки")
    failed_groups = []
    # Отправляем сообщение во все группы
    for idx, group in enumerate(groups, start=1):
        try:
            await client.send_message(group, final_text)
            print(f"✅ [{idx}/{len(groups)}] Отправлено в {group}")
        except Exception as e:
            print(f"❌ Ошибка в {group}: {e}")

        # Рандомная задержка (3–7 секунд)
        delay = random.randint(1, 3)
        print(f"⏳ Ждём {delay} сек перед следующим сообщением...")
        await asyncio.sleep(delay)

        print("\n📊 Результаты:")
        print(f"Успешно: {len(groups) - len(failed_groups)}")
        print(f"Ошибок: {len(failed_groups)}")

with client:
    client.loop.run_until_complete(main())
