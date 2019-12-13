from pyrogram import Client, Filters
k = -1001350799105
bot = "1025449281:AAF2ZNFJdjP7Uh-XjyLIJ8LRFTnXsrrZrwQ"
app = Client (session_name="rr",api_id=814511,api_hash="44462f0f278503255d5cc30941b617a9",bot_token = bot)                                   
bullet = -1001428773103                                              
ferrari = -1001421693753                                             
@app.on_message(Filters.chat(ferrari) & ~ Filters.edited)
def main(client, message):
 client.send_message( k,message.text.markdown)
@app.on_message(Filters.chat(bullet) & ~ Filters.edited)
def main(client, message):
 client.send_message( k,message.text.markdown)
app.run()
