from pyrogram import Client, Filters,Emoji
app = Client("mcc",715451,"d2cba6f7bf5d1a45682da5bb9071a307")
k = -1001453099412
@app.on_message( Filters.text & ~Filters.edited & Filters.channel)
def forward(client, message):
 fil = open("source.txt" , "r")
 lins = fil.readlines()
 fil.close()
 for t in lins:
  if int(t) == message.chat.id:
    f = False
    words = ['dekho','TRUST','join','fix','😱','😳','👆','👇','☝️','https://','😂','🤔','pass','chase','link','suno','member','❓','loss','audio','open',"report",'paid','contact','baazigar','market','load','whatsapp','book','bhai','🐴','only','chut','tennis','teen','lavde','chutiya','bc','kya','line','LUND','WICKET LU','?','loda','telegram','chor',"kama","lakh",' id','स',"kitna"]
    for word in words:
     if word.casefold() in message.text.casefold():
      return
    client.send_message(k,message.text)   

@app.on_message(Filters.command("setf"))
def forward(client, message):
  with open("source.txt" , "w") as file:
   file.write(message.text.split(' ')[1])
   file.close()
   message.reply("done bro ₹₹₹₹ ")
app.run()
