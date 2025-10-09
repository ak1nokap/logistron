import asyncio
import random
from telethon import TelegramClient

# ⚡ Данные API (с сайта https://my.telegram.org)
api_id = 23506845
api_hash = "a015ff48c31ca309a5ef6543f8fe65dd"

client = TelegramClient("session_name", api_id, api_hash)



async def main():

    # Получаем последнее сообщение из Избранного
    msg = await client.get_messages("me", limit=1)
    if not msg:
        print("❌ В Избранном нет сообщений!")
        return

    source_msg = msg[0]
    print(f"🆔 Найдено сообщение {source_msg.id}: {source_msg.text[:50]}...")

    # Читаем список групп из файла
    with open("groups.txt", "r", encoding="utf-8") as f:
        groups = [line.strip() for line in f if line.strip()]

    print(f"📢 Найдено {len(groups)} групп для рассылки")
    failed_groups = []
    # Пересылаем сообщение
    for idx, group in enumerate(groups, start=1):
        try:
            await client.forward_messages(group, source_msg.id, "me")
            print(f"✅ [{idx}/{len(groups)}] Переслано в {group}")
        except Exception as e:
            print(f"❌ Ошибка в {group}: {e}")
            failed_groups.append(group)

        #Рандомная задержка (3–8 секунд)
        delay = random.randint(3, 8)
        print(f"⏳ Ждём {delay} сек...")
        await asyncio.sleep(delay)

        print("\n📊 Результаты:")
        print(f"Успешно: {len(groups) - len(failed_groups)}")
        print(f"Ошибок: {len(failed_groups)}")

with client:
    client.loop.run_until_complete(main())

