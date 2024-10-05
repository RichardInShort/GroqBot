import sqlite3
import app.keyboards as kb
from aiogram import filters, types, Router
from app.aifuncs import groqreply

conn = sqlite3.connect('chat.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS messages (
        id INTEGER PRIMARY KEY,
        chat_id INTEGER,
        user_id INTEGER,
        text TEXT,
        reply TEXT,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    )
''')
conn.commit()
conn.close()

router = Router()


async def save_message(message: types.Message, reply):
    conn = sqlite3.connect('chat.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO messages (chat_id, user_id, text, reply)
        VALUES (?, ?, ?, ?)
    ''', (message.chat.id, message.from_user.id, message.text, reply))

    conn.commit()
    conn.close()

    #await message.answer('Сообщение сохранено!')


@router.message(filters.Command('start'))
async def start_cmd(message: types.Message):
    markup = kb.inlinestartkb
    await message.answer(f'Бот запущен, {message.chat.first_name}')
    await message.answer('Groq.cloud :point_down:', reply_markup=markup)

@router.message(filters.Command('delete'))
async def delete_cmd(message: types.Message):
    conn = sqlite3.connect('chat.db')
    cursor = conn.cursor()
    user_id = message.from_user.id
    conn.commit()
    cursor.execute('DELETE FROM messages WHERE user_id = ?', (user_id,))
    conn.commit()
    conn.close()
    markup = kb.inlinestartkb
    await message.answer(f'Сообщения удалены', reply_markup=markup)

@router.message()
async def reply(message: types.Message):
    reply = await groqreply(message)
    await message.answer(reply)
    await save_message(message, reply)