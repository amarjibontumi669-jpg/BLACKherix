from pyrogram import Client, filters
import asyncio

# আপনার তথ্য
API_ID = 39106926
API_HASH = "191ea45ffa486ac5afb6486a8cf8e013"

app = Client("my_assistant", api_id=API_ID, api_hash=API_HASH)

# মেসেজ ট্র্যাক করার জন্য
waiting_list = {}

# আরও স্টাইলিশ এবং ফাঁকা ফাঁকা অটো মেসেজ
AUTO_MESSAGE = (
    "<b>⚡ ᴀssᴀʟᴀᴍᴜ ᴀʟᴀɪᴋᴜᴍ sɪʀ ⚡</b>\n\n\n"
    "🤖 আমি হলাম <b>ʙʟᴀᴄᴋ ʜᴇʀɪx</b> এর\n"
    "পার্সোনাল অ্যাসিস্ট্যান্ট বট।\n\n\n"
    "🕵️ উনি এখন লাইনে নাই,\n"
    "লাইনে আসলে উনি আপনাকে রিপ্লাই দিবেন।\n\n\n"
    "📢 <b>ᴍʏ ᴄʜᴀɴɴᴇʟ:</b>\n"
    "👉 <a href='https://t.me/+ngz1XdQWVPMxYWE1'>ᴄʟɪᴄᴋ ʜᴇʀᴇ ᴛᴏ ᴊᴏɪɴ</a>\n\n"
    "────────────────────\n"
    "📟 <i>sʏsᴛᴇᴍ: sᴛᴀɴᴅʙʏ ᴍᴏᴅᴇ...</i>"
)

@app.on_message(filters.private & ~filters.me)
async def auto_reply(client, message):
    user_id = message.from_user.id
    
    if user_id not in waiting_list:
        waiting_list[user_id] = True
        
        # ১৫ সেকেন্ড অপেক্ষা করবে (আপনার অনুরোধ অনুযায়ী)
        await asyncio.sleep(15)
        
        # ১৫ সেকেন্ড পর যদি আপনি রিপ্লাই না দিয়ে থাকেন
        if user_id in waiting_list:
            try:
                await message.reply_text(AUTO_MESSAGE, disable_web_page_preview=False)
            except Exception as e:
                print(f"Error: {e}")
            
            del waiting_list[user_id]

@app.on_message(filters.private & filters.me)
async def me_replied(client, message):
    # আপনি নিজে মেসেজ দিলে টাইমার ক্যানসেল হবে
    user_id = message.chat.id
    if user_id in waiting_list:
        del waiting_list[user_id]

print("✅ Black Herix Assistant Bot is Running (15s Timer)...")
app.run()
from pyrogram import Client, filters
import asyncio

# আপনার তথ্য
API_ID = 39106926
API_HASH = "191ea45ffa486ac5afb6486a8cf8e013"

app = Client("my_assistant", api_id=API_ID, api_hash=API_HASH)

# মেসেজ ট্র্যাক করার জন্য
waiting_list = {}

# আরও স্টাইলিশ এবং ফাঁকা ফাঁকা অটো মেসেজ
AUTO_MESSAGE = (
    "<b>⚡ ᴀssᴀʟᴀᴍᴜ ᴀʟᴀɪᴋᴜᴍ sɪʀ ⚡</b>\n\n\n"
    "🤖 আমি হলাম <b>ʙʟᴀᴄᴋ ʜᴇʀɪx</b> এর\n"
    "পার্সোনাল অ্যাসিস্ট্যান্ট বট।\n\n\n"
    "🕵️ উনি এখন লাইনে নাই,\n"
    "লাইনে আসলে উনি আপনাকে রিপ্লাই দিবেন।\n\n\n"
    "📢 <b>ᴍʏ ᴄʜᴀɴɴᴇʟ:</b>\n"
    "👉 <a href='https://t.me/+ngz1XdQWVPMxYWE1'>ᴄʟɪᴄᴋ ʜᴇʀᴇ ᴛᴏ ᴊᴏɪɴ</a>\n\n"
    "────────────────────\n"
    "📟 <i>sʏsᴛᴇᴍ: sᴛᴀɴᴅʙʏ ᴍᴏᴅᴇ...</i>"
)

@app.on_message(filters.private & ~filters.me)
async def auto_reply(client, message):
    user_id = message.from_user.id
    
    if user_id not in waiting_list:
        waiting_list[user_id] = True
        
        # ১৫ সেকেন্ড অপেক্ষা করবে (আপনার অনুরোধ অনুযায়ী)
        await asyncio.sleep(15)
        
        # ১৫ সেকেন্ড পর যদি আপনি রিপ্লাই না দিয়ে থাকেন
        if user_id in waiting_list:
            try:
                await message.reply_text(AUTO_MESSAGE, disable_web_page_preview=False)
            except Exception as e:
                print(f"Error: {e}")
            
            del waiting_list[user_id]

@app.on_message(filters.private & filters.me)
async def me_replied(client, message):
    # আপনি নিজে মেসেজ দিলে টাইমার ক্যানসেল হবে
    user_id = message.chat.id
    if user_id in waiting_list:
        del waiting_list[user_id]

print("✅ Black Herix Assistant Bot is Running (15s Timer)...")
app.run()
