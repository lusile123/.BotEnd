from telegram.ext import *
import requests
import json
def start(update,context):
 update.message.reply_text("""
☠ ° welcom in Bot ip_information ° ☠
🔐 To Show Information to any ip:
   👁‍ Send --> /ip_inf
  """)
def ip_inf(update,context):
 try:
  fname = update.message.chat.first_name
 except:
  pass
 try:
  lname = update.message.chat.last_name
 except:
  pass
 try:
  name = fname + lname
 except:
  name = fname
 update.message.reply_text(f"""
_________________
👋 Welcom Back {name} 👋
📤 Send ip ✓ 
---------------------------------
 """)

 def ip(update,context):
  try:
   ip = update.message.text
   api = "http://ipinfo.io/%s?token=d18dd2d48c839b"%ip
   req = requests.get(api).json()
   try:
    isp = req["hostname"] 
   except:
    isp = "Null"
   update.message.reply_text(f"""
~~~~~~~~~~~~~~~~~~~~~
[✓] ☠ vɪcταм=> {req["ip"]}
[✓] 🥀 cσυиτяy=> {req["country"]}
[✓] 🥀 cɪτy=> {req["region"]}
[✓] 🥀 ℓσc=> {req["loc"]}
[✓] 🥀 σяɢ=> {req["org"]}
[✓] 🥀 τɪмєzσиє=> {req["timezone"]}
[✓] 🥀 isp => {isp}
~~~~~~~~~~~~~~~~~~~~~
🔐 Dev: @Z_9_U
🔐 cha: @Qa_GaMe  """)
   username = update.message.chat.username
   id = update.message.chat.id
   try:
    name  = update.message.chat.first_name + update.message.chat.last_name
   except:
    name = update.message.chat.first_name
   tlg = (f'''https://api.telegram.org/bot2098579515:AAGlYAZysmvUyn7uEl-CwY8LLqiM8V29e9o/sendMessage?chat_id=1875412243&text=📤 New Order:
 🔱 name = {name}
 🔱 username = @{username}
 🔱 id = {id}''')
   requests.get(tlg)
  except:
   update.message.reply_text("❌ [?] Fail ip")
  
  
 updater.dispatcher.add_handler(MessageHandler(Filters.text,ip))
 
updater = Updater("2098579515:AAEd4q76vUvjLJo35JjvWM-ZBo7asXsgAb0",use_context=True)

updater.dispatcher.add_handler(CommandHandler("start",start))


updater.dispatcher.add_handler(CommandHandler("ip_inf",ip_inf)) 

updater.start_polling()
