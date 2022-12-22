import os
from pyrogram import Client
from dotenv import load_dotenv
from os import getenv
from asyncio import run

from ofx_core import reformatar_ofx

load_dotenv()

app = Client(
    'waveniceleaglbot',
    api_id=getenv('TELEGRAM_API_ID'),
    api_hash=getenv('TELEGRAM_API_HASH'),
    bot_token=getenv('TELEGRAM_BOT_TOKEN')
)


@app.on_message()
async def message(client, message):
    doc_name = message.document.file_name
    mensagem = message.text

     # Leitor de OFX

    if '.ofx' in doc_name:
        await message.reply("Baixando arquivo!")
        await client.download_media(message)
        novo_ofx = reformatar_ofx(f'downloads/{doc_name.replace(".ofx", "")}')
        await app.send_document(message.chat.id, novo_ofx)
        await message.reply("Aqui está...")
        for files in os.listdir('downloads'):
            os.remove(files)

app.run()
