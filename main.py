
import telepot, time 
import os
TOKEN = os.environ.get('BOT_TOKEN')

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    print ('Got command: %s' % command)

    if command == '/hello':
        bot.sendMessage(chat_id, "Hello, how are you?")

# Create a bot object with API key
bot = telepot.Bot(TOKEN)
bot.message_loop(handle)

print('Listening ...')
# Listen to the messages
while 1:
    time.sleep(5)