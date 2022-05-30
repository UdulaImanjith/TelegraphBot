#Copyright ©️ 2022 TeLe TiPs. All Rights Reserved
#You are free to use this code in any of your project, but you MUST include the following in your README.md (Copy & paste)
# ##Credits - [MediaToTelegraphLink bot by TeLe TiPs] (https://github.com/teletips/MediaToTelegraphLink-TeLeTiPs)

from pyrogram import Client, filters
from pyrogram.types import Message
from telegraph import upload_file
import os

teletips=Client(
    "MediaToTelegraphLink",
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"],
    bot_token = os.environ["BOT_TOKEN"]
)

@teletips.on_message(filters.command('start') & filters.private)
async def start(client, message):
    text = f"""
ʜᴇʏ ᴛʜᴇʀᴇ {message.from_user.mention} 👋,
ɪ ᴄᴀɴ ᴇᴀꜱɪʟʏ ɢᴇɴᴇʀᴀᴛᴇ ᴛᴇʟᴇɢʀᴀᴘʜ ʟɪɴᴋꜱ ꜰᴏʀ ʏᴏᴜʀ ᴍᴇᴅɪᴀ ꜰɪʟᴇꜱ 📥

ʏᴏᴜ ᴊᴜꜱᴛ ʜᴀᴠᴇ ᴛᴏ ꜱᴇɴᴅ ᴀ ᴠᴀʟɪᴅ ᴍᴇᴅɪᴀ ꜰɪʟᴇ ᴀɴᴅ ɪ ᴡɪʟʟ ᴅᴏ ᴛʜᴇ ʀᴇꜱᴛ 😏
➡ (ᴠᴀʟɪᴅ ꜰɪʟᴇ ᴛʏᴘᴇꜱ ᴀʀᴇ ᴊᴘᴇɢ', 'ᴊᴘɢ', 'ᴘɴɢ', 'ᴍᴘ4' ᴀɴᴅ 'ɢɪꜰ')

💠 ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ʟɪɴᴋꜱ ɪɴ **ɢʀᴏᴜᴘ ᴄʜᴀᴛꜱ**, ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ꜱᴜᴘᴇʀɢʀᴏᴜᴘ ᴀɴᴅ ꜱᴇɴᴅ ᴛʜᴇ ᴄᴏᴍᴍᴀɴᴅ <code>/tl</code> ᴀꜱ ᴀ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴠᴀʟɪᴅ ᴍᴇᴅɪᴀ ꜰɪʟᴇ.

👤 | ᴅᴇᴠᴇʟᴏᴘᴇᴅ ʙʏ [ɴᴇxᴜꜱ 💫](https://t.me/Nexus_8)
💫 | ᴘʀᴏᴊᴇᴄᴛ ʙʏ [ɪꜱᴏᴛʀᴏᴘ ᴄᴏᴍᴍᴜɴɪᴛʏ](https://t.me/isotrop)
            """
    await teletips.send_message(message.chat.id, text, disable_web_page_preview=True)
    

@teletips.on_message(filters.media & filters.private)
async def get_link_private(client, message):
    try:
        text = await message.reply("Processing...")
        async def progress(current, total):
            await text.edit_text(f"📥 ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ ᴍᴇᴅɪᴀ... {current * 100 / total:.1f}%")
        try:
            location = f"./media/private/"
            local_path = await message.download(location, progress=progress)
            await text.edit_text("📤 ᴜᴘʟᴏᴀᴅɪɴɢ ᴛᴏ ᴛᴇʟᴇɢʀᴀᴘʜ...")
            upload_path = upload_file(local_path) 
            await text.edit_text(f"**🌐 | ᴛᴇʟᴇɢʀᴀᴘʜ ʟɪɴᴋ**:\n\n<code>https://telegra.ph{upload_path[0]}</code>\n\n©️ [ɪꜱᴏᴛʀᴏᴘ ᴄᴏᴍᴍᴜɴɪᴛʏ](https://t.me/isotrop)")     
            os.remove(local_path) 
        except Exception as e:
            await text.edit_text(f"**❌ | ꜰɪʟᴇ ᴜᴘʟᴏᴀᴅ ꜰᴀɪʟᴇᴅ**\n\n<i>**Reason**: {e}</i>\n\n©️ [ɪꜱᴏᴛʀᴏᴘ ᴄᴏᴍᴍᴜɴɪᴛʏ](https://t.me/isotrop)")
            os.remove(local_path) 
            return                 
    except Exception:
        pass        

@teletips.on_message(filters.command('tl'))
async def get_link_group(client, message):
    try:
        text = await message.reply("Processing...")
        async def progress(current, total):
            await text.edit_text(f"📥 ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ ᴍᴇᴅɪᴀ... {current * 100 / total:.1f}%")
        try:
            location = f"./media/group/"
            local_path = await message.reply_to_message.download(location, progress=progress)
            await text.edit_text("📤 ᴜᴘʟᴏᴀᴅɪɴɢ ᴛᴏ ᴛᴇʟᴇɢʀᴀᴘʜ...")
            upload_path = upload_file(local_path) 
            await text.edit_text(f"**🌐 | ᴛᴇʟᴇɢʀᴀᴘʜ ʟɪɴᴋ**:\n\n<code>https://telegra.ph{upload_path[0]}</code>\n\n©️ [ɪꜱᴏᴛʀᴏᴘ ᴄᴏᴍᴍᴜɴɪᴛʏ](https://t.me/isotrop)")     
            os.remove(local_path) 
        except Exception as e:
            await text.edit_text(f"**❌ | ꜰɪʟᴇ ᴜᴘʟᴏᴀᴅ ꜰᴀɪʟᴇᴅ**\n\n<i>**Reason**: {e}</i>\n\n©️ [ɪꜱᴏᴛʀᴏᴘ ᴄᴏᴍᴍᴜɴɪᴛʏ](https://t.me/isotrop)")
            os.remove(local_path) 
            return         
    except Exception:
        pass                                           

print("Bot is alive!")
teletips.run()

#Copyright ©️ 2022 TeLe TiPs. All Rights Reserved
