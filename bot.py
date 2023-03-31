import asyncio,os
import json
from telethon.sessions import StringSession
from telethon import TelegramClient, events
api_id = 15258706
api_hash = 'a42b37363abecdc4ccb2196ed072ddf2'
string = "1ApWapzMBu5F6lzuWUCrtZDBNumhDjcSESxGFYHgyH2a4zFGsI4N1KOUVvUWfLLpygLoLn1lQYcy6yrQZTzKi137eWMAHjUbcaIQepYPOJvXfEX_RSBHpUJoJQA7x2PMOgIKtzpV1xN5HeQ8kFYzMmHkG7L01kWXnXcGi-auiZjBOTICezloi_d6IWfzjBxiEQEuPvTG-9B6-_KgryIgPlj7JpI51VLMDcUF6vmbhuOsqzG5JLhyS77pTWgERZFuyB4P5yb8IFEnhsAqGSd40J7g3iBlNc3ys3JHPPGUafMPmoiX40zTD_h_-YhVS1gTTOotdLODR-il25pcCdjDavmVlEFvTBNk="
client = TelegramClient(StringSession(string), api_id, api_hash)
data = {}
def savejson(texxt):
    A = texxt.split("dkejofhwkfnwkjfkwnfksjfjr")
    if len(A) == 1:
        A1 = A[0]
        if A1 in data and data[A1] != "empty":
            pass
        else:
            data[A1] = "empty"
    elif len(A) == 2:
        A1 = A[0]
        A2 = A[1]
        if A1 in data:
            if A2 not in data[A1] and A2 != ' ':
                data[A1].append(A2)
        else:
            if A2 != ' ':
                data[A1] = [A2]

    output = json.dumps(data, ensure_ascii=False)
    return output

    


@client.on(events.NewMessage)
async def my_event_handler(event):
 avent=event.message
 while True:
  try:
    if str(avent.reply_to)=="None":
     print(savejson(avent.message.message))
     break
    else:
    
     idmsreply=avent.reply_to.reply_to_msg_id
     oildtext=avent.message
     avent = await client.get_messages(1938276557, ids=idmsreply)
     
     savejson(f"""{avent.message}dkejofhwkfnwkjfkwnfksjfjr{oildtext}""")
  except Exception as e:
   if avent.reply_to==None:
    
    open("dump.json","w").write(str(savejson(avent.message)))

    break
   else:
    print("error"+e)
async def main():
    await client.start()
    await client.run_until_disconnected()

print("start")
if __name__ == '__main__':
    asyncio.run(main())

