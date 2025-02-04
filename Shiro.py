# meta developer: Prinz Eugen

import asyncio
from .. import loader, utils
import random

@loader.tds
class Shiro(loader.Module):
    """Широ, незаменимый помощник"""
    strings = {"name": "Shiro"}

    @loader.command()
    async def Широcmd(self, message):
        """Просмотр профиля Широ"""

        farm_muku_status = "<emoji document_id=5316906020499365122>✔️</emoji> Приглядываю за курочками" if self.get("farm_muku", False) else "<emoji document_id=5314766675814394234>❎</emoji> Не приглядываю за курочками"
        farm_muko_status = "<emoji document_id=5316906020499365122>✔️</emoji> Приглядываю за колодцем" if self.get("farm_moko", False) else "<emoji document_id=5314766675814394234>❎</emoji> Не приглядываю за колодцем"
        farm_mug_status = "<emoji document_id=5316906020499365122>✔️</emoji> Приглядываю за грядками" if self.get("farm_mug", False) else "<emoji document_id=5314766675814394234>❎</emoji> Не приглядываю за грядками"
        
        await message.reply(
            "<b>🌘 Широ</b>\n\n"
            "<b><emoji document_id=6325682031741109665>💃</emoji> Создатель:</b> <b>𝙋𝙧𝙞𝙣𝙯 𝙀𝙪𝙜𝙚𝙣</b>\n\n"
            "<b>💫 Версия:</b> <i>1.0.9</i>\n"
            "<b>🌳 Ветка:</b> <code>v1.0.9</code>\n"
            "😌 <b>Актуальная версия</b>\n\n"
            f"{farm_muku_status}\n"
            f"{farm_muko_status}\n"
            f"{farm_mug_status}",
            link_preview=False,
            file="https://i.ibb.co/MSbymFB/IMG-5508.jpg"
        )
        await message.delete()


    async def мукоcmd(self, message):
        """авто колодец"""
        farm_status = self.get("farm_moko", False)

        if farm_status:
            self.set("farm_moko", False)
            await utils.answer(message, f"<emoji document_id=5314766675814394234>❎</emoji>Не набираем ведра.")
        else:
            self.set("farm_moko", True)
            await utils.answer(message, f"<emoji document_id=5316906020499365122>✔️</emoji>Набираем ведра.")

            while self.get("farm_moko"):
                await message.client.send_message(1606812809, "муко")
                await asyncio.sleep(5)  # Небольшая пауза перед проверкой

                # Получаем последние сообщения из чата с ID 1606812809
                chat_messages = await message.client.get_messages(1606812809, limit=5)
                for msg in chat_messages:
                    if msg.reply_markup and '🛢' in msg.text:
                        buttons = msg.reply_markup.rows
                        if len(buttons) > 0:  # Проверяем, что есть кнопка с индексом 1
                            await msg.click(0)  # Нажимаем на кнопку с индексом 1
                            break  # Выход из цикла после нажатия на кнопку
                        
                await asyncio.sleep(random.randint(10800, 14400))

    
    async def мукуcmd(self, message):
        """авто курятник"""
        farm_status = self.get("farm_muku", False)

        if farm_status:
            self.set("farm_muku", False)
            await utils.answer(message, "<emoji document_id=5314766675814394234>❎</emoji> Не собираем яйца.")
        else:
            self.set("farm_muku", True)
            await utils.answer(message, "<emoji document_id=5316906020499365122>✔️</emoji> Собираем яйца.")

            while self.get("farm_muku"):
                await message.client.send_message(1606812809, "муку")
                await asyncio.sleep(5)  # Небольшая пауза перед проверкой

                # Получаем последние сообщения из чата с ID 1606812809
                chat_messages = await message.client.get_messages(1606812809, limit=5)
                for msg in chat_messages:
                    if msg.reply_markup and '✨💕' in msg.text:
                        buttons = msg.reply_markup.rows
                        if len(buttons) > 0:
                            await msg.click(0)
                            await asyncio.sleep(2)
                            await msg.click(1)
                            await asyncio.sleep(2)
                            await msg.click(3)
                            break
                            
                await asyncio.sleep(random.randint(7380, 7820))


    async def мувcmd(self, message):
        """автомасло"""
        farm_status = self.get("farm_muv", False)

        if farm_status:
            self.set("farm_muv", False)
            await utils.answer(message, f"<emoji document_id=5314766675814394234>❎</emoji>Не крафтим.")
        else:
            self.set("farm_muv", True)
            await utils.answer(message, f"<emoji document_id=5314766675814394234>✔️</emoji>Крафтим.")
            
            while self.get("farm_muv"):
                await message.client.send_message(-1002061336473, "мув")
                await asyncio.sleep(5)

                chat_messages = await message.client.get_messages(-1002061336473, limit=5)
                for msg in chat_messages:
                    if msg.reply_markup and '🧤' in msg.text:
                        buttons = msg.reply_markup.rows
                        for row in buttons:
                            for button in row.buttons:
                                if '🔥' in button.text:
                                    msg = await message.client.get_messages(msg.chat_id, ids=msg.id)
                                    await msg.click(0)
                                    await asyncio.sleep(2)
                                    msg = await message.client.get_messages(msg.chat_id, ids=msg.id)
                                    await msg.click(0)
                                    msg = await message.client.get_messages(msg.chat_id, ids=msg.id)
                                    await msg.reply("50")
                                    await asyncio.sleep(random.randint(1920, 2100))
                                    break
                                elif '👋🏻' in button.text:
                                    await msg.click(0)
                                    break
                await asyncio.sleep(5)         

    async def цыпcmd(self, message):
        """обмен цып"""

        sent_message = await message.respond("кинуть цыпу", reply_to=message.id) 
        await asyncio.sleep(2)
        updates = await self._client.get_messages(message.peer_id, limit=2)
        for msg in updates:
            if msg.buttons:
                if msg.buttons:
                    try:
                        await msg.click(0)
                        return  # Завершаем функцию после нажатия кнопки
                    except Exception as e:
                        await message.reply(f"Ошибка при нажатии кнопки: {e}")
                        return

    async def куряcmd(self, message):
        """разовый сбор курей"""

        await utils.answer(message, "муку")
        await asyncio.sleep(2)
        updates = await self._client.get_messages(message.peer_id, limit=2)
        for msg in updates:
             if msg.buttons:
                 if msg.buttons:
                     try:
                         await msg.click(0)
                         return  # Завершаем функцию после нажатия кнопки
                     except Exception as e:
                         await message.reply(f"Ошибка при нажатии кнопки: {e}")
                         return
        

    async def мугcmd(self, message):
        """авто грядки"""
        farm_status = self.get("farm_mug", False)

        if farm_status:
            self.set("farm_mug", False)
            await utils.answer(message, f"<emoji document_id=5314766675814394234>❎</emoji>Не растим.")
        else:
            self.set("farm_mug", True)
            await utils.answer(message, f"<emoji document_id=5316906020499365122>✔️</emoji>Растим.")

            # Начинаем работу с фермой
            await self.run_farm_cycle(message)

    async def run_farm_cycle(self, message):
        """Запускает цикл работы с фермой"""
        while self.get("farm_mug"):  # Бесконечный цикл для работы с фермой
            await message.client.send_message(1606812809, "муг")
            await asyncio.sleep(5)  # Небольшая пауза перед проверкой

            chat_messages = await message.client.get_messages(1606812809, limit=5)
            for msg in chat_messages:
                if msg.reply_markup and '🧑🏻‍🌾' in msg.text:
                    buttons = msg.reply_markup.rows
                    for row in buttons:
                        for button in row.buttons:
                            if '💗' in button.text:
                                # Обрабатываем клики для полянок
                                await self.process_garden(msg, [0, 9, 6, 6, 4, 11, 10])
                                await self.process_garden(msg, [1, 9, 6, 6, 4, 11, 10])
                                await self.process_garden(msg, [2, 9, 6, 6, 4, 11, 10])
                                await self.process_garden(msg, [3, 9, 6, 6, 4, 11, 10])
                                await self.reset_and_wait(message)  # Сбрасываем состояние и возвращаемся к циклу
                                break
                            elif '⌛️' in button.text:
                                await self.process_garden(msg, [0, 11, 10])
                                await self.process_garden(msg, [1, 11, 10])
                                await self.process_garden(msg, [2, 11, 10])
                                await self.process_garden(msg, [3, 11, 10])
                                await self.reset_and_wait(message)  # Сбрасываем состояние и возвращаемся к циклу
                                break

    async def process_garden(self, msg, indices):
        """Обрабатывает клики на полянках"""
        for index in indices:
            try:
                await msg.click(index)
                await asyncio.sleep(2)
                msg = (await msg.client.get_messages(msg.chat_id, ids=msg.id))
            except IndexError:
                print(f"Индекс {index} вне диапазона для текущего сообщения")

    async def reset_and_wait(self, message):
        """Сбрасывает состояние и ожидает 20-25 минут перед повтором"""
        await asyncio.sleep(random.randint(1200, 1500))  # Задержка 20-25 минут перед следующим запуском
        print("Таймер завершен, продолжаем с отправки 'муг'.")
        # После завершения ожидания снова запускаем цикл
        await self.run_farm_cycle(message)  # Перезапускаем цикл
