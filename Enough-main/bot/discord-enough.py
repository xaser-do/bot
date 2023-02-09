import discord
from time import sleep
from requests import get
r = get("https://raw.githubusercontent.com/tingirifistik/Enough/main/sms.py").text
with open("sms.py", "r", encoding="utf-8") as f:
    read = f.read()
if read == r:
    pass
else:
    print("Güncelleme yapılıyor...")
    with open("sms.py", "w", encoding="utf-8") as f:
        f.write(r)
from sms import SendSms

token = "ODIzNDk5MzQ1MjA5OTgyOTk2.GNLiPN.xrlvElqhFi5iCruwBpjZJsuv6wkjluuf64_25Y"
gif = "https://media1.giphy.com/media/dK0tjRx03fhlK/giphy.gif?cid=ecf05e47fr8gh07yh4ovynw6y1o0by6gft63yqd0gi8elxwu&rid=giphy.gif&ct=g"
adet = 55
saniye = 0

intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('{} Çalışmaya Başladı!'.format(client.user))
    activity = discord.Activity(type=discord.ActivityType.playing, name="by xaser")
    await client.change_presence(activity=activity)
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if len(message.content.split(" ")) == 2 and message.content.split(" ")[0] == "*sms":
        if len(message.content.split(" ")[1]) == 10:
            telno = message.content.split(" ")[1]
            embed=discord.Embed(title="HAKKİ GOTTEN YESSİR", description=(f"{adet} hakki yarami yessir SMS Gönderiliyor --> {telno}\n{message.author.mention}"), color=0x001eff)
            embed.set_thumbnail(url=gif)
            await message.channel.send(embed=embed)
            sms = SendSms(telno, "")
            while sms.adet < adet:
                for attribute in dir(SendSms):
                    attribute_value = getattr(SendSms, attribute)
                    if callable(attribute_value):
                        if attribute.startswith('__') == False:
                            if sms.adet == adet:
                                break
                            exec("sms."+attribute+"()")
                            sleep(saniye)
            await message.channel.send(telno+" --> "+str(sms.adet)+f" adet SMS gönderildi.\n{message.author.mention}")                        
        else:
            await message.channel.send(f"Geçerli komut yazınız!\nYardım için ' *help ' yazınız.\n{message.author.mention}")
    elif "*help" == message.content:
        await message.channel.send(f"Sms göndermek için komutu aşağıdaki gibi yazınız.\n```*sms 5051234567```\n*sms (telefon numarası)\n{message.author.mention}")
    else:
        pass
  
client.run(token)