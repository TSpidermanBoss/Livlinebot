from pyrogram import Client, Filters
from pyrogram.errors import FloodWait
import time
app = Client("122",1115222,"b5d91575831ac4ffb32d6bcc8056f722")
s = -1001062910865
d = -1001278248820
@app.on_message(Filters.chat(s) & Filters.text & ~Filters.edited)
def forward(client,Message):
 f = False
 words = ['dekho','TRUST','join','fix','😱','😳','👆','👇','☝️','https://','😂','🤔','pass','chase','link','suno','member','❓','loss','audio','open',"report",'paid','contact','baazigar','market','load','whatsapp','book','bhai','🐴','only','chut','tennis','teen','lavde','chutiya','bc','kya','line','LUND','WICKET LU','?','loda','telegram','chor',"kama","lakh",' id','स',"kitna"]
 for word in words:
  if word.casefold() in Message.text.casefold():
    return
 client.send_message(d, Message.text.markdown)
app.run()
