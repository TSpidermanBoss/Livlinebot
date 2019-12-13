from pyrogram import Client, Filters
from pyrogram.errors import FloodWait
import time
app = Client("s",965018,"6cd1a0cfc1a3e76076a8331c4319e97c")
s = -1001062910865
d = -1001403061160
@app.on_message(Filters.chat(s) & Filters.text & ~Filters.edited)
def forward(client,Message):
 f = False
 words = ['dekho','TRUST','join','fix','😱','😳','👆','👇','☝️','https://','😂','🤔','pass','chase','link','suno','member','❓','loss','audio','open',"report",'paid','contact','baazigar','market','load','whatsapp','book','bhai','🐴','only','chut','tennis','teen','lavde','chutiya','bc','kya','line','LUND','WICKET LU','?','loda','telegram','chor',"kama","lakh",' id','स',"kitna"]
 for word in words:
  if word.casefold() in Message.text.casefold():
    return
 client.send_message(d, Message.text.markdown)
app.run()
