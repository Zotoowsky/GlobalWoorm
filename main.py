import asyncio
from asyncio import tasks
import random
import discord
from discord.ext import commands
import requests

intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix='@', intents=intents)\


questions = {
    "Какой газ является основной причиной глобального потепления?": "Диоксид углерода (CO2)",
    "Как называется явление, при котором ледники тают из-за повышения температуры Земли?": "Таяние ледников",
    "Какой цвет имеет небо в ясный солнечный день?": "голубой",
    "Какие основные источники выбросов парниковых газов?" : "Автомобили, энергетика, промышленность, сельское хозяйство и т. д.",
    "Что такое эффект парникового газа?" : "Эффект парникового газа - это явление удержания тепловой энергии в атмосфере Земли, что приводит к повышению температуры планеты.",
    "Какое воздействие глобального потепления оказывает на экосистемы и животных?" : "Глобальное потепление может привести к изменению климата, массовому вымиранию видов, изменению водных ресурсов и увеличению частоты экстремальных погодных явлений."
    
}
def carbon_footprint_tips():
    tips = [
        "Используйте общественный транспорт или делитесь поездками с коллегами, чтобы уменьшить выбросы от автотранспорта.",
        "Переходите на энергоэффективные лампочки и бытовую технику для снижения энергопотребления.",
        "Покупайте продукты местного производства, чтобы уменьшить транспортные расходы и выбросы углекислого газа.",
        "Сократите потребление пластика и других одноразовых материалов, используя перерабатываемые альтернативы.",
        "Участвуйте в программе посадки деревьев или создайте собственный мини-сад на балконе или во дворе."
    ]
    
    return random.choice(tips)

def climate_change_info():
    climate_change_info = {
        "Причины глобального потепления": "Главной причиной глобального потепления считается увеличение выбросов парниковых газов в атмосферу, таких как углекислый газ и метан, в результате деятельности человека, включая сжигание ископаемых топлив, вырубку лесов и промышленные процессы.",
        "Последствия глобального потепления": "Глобальное потепление приводит к изменению климата, что в свою очередь вызывает учащение экстремальных погодных явлений, повышение уровня морей и океанов, уменьшение ледников и снежного покрова, а также угрозу для биоразнообразия и сельского хозяйства.",
        "Меры по борьбе с глобальным потеплением": "Для снижения негативных последствий глобального потепления необходимо принимать меры по уменьшению выбросов парниковых газов, повышению энергоэффективности, использованию возобновляемых источников энергии, сохранению лесов и принятию мер по адаптации к изменениям климата."
    }
    
    return climate_change_info

eco_challenges = [
    "Проведите день без использования пластиковых изделий.",
    "Посадите дерево или цветы в своем районе.",
    "Соберите мусор на улице или в парке.",
    "Сократите потребление воды на день.",
    "Изучите возможности утилизации отходов в вашем городе."
]



@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def hello(ctx):
    await ctx.send('Привет! Я эко-бот и работаю в области проблем "Глобальное потепление", Спасибо что пользуетесь моими услугами!')

@bot.command(name = "Викторина")
async def quiz(ctx):
    question = random.choice(list(questions.keys()))
    answer = questions[question]   

    await ctx.send(question)

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    try:
        user_answer = await bot.wait_for('message', check=check, timeout=20)
    except asyncio.TimeoutError:
        await ctx.send(f"Время вышло! Правильный ответ: {answer}")
        return

    if user_answer.content == answer:
        await ctx.send(f"Правильно, {ctx.author.mention}!")
    else:
        await ctx.send(f"Неверно. Правильный ответ: {answer}")

@bot.command()
async def eco_tips(ctx):
    tip = carbon_footprint_tips()
    await ctx.send(f'Совет для уменьшения углеродного следа: {tip}')  

@bot.command()
async def show_image(ctx):
        await ctx.send('https://cf2.ppt-online.org/files2/slide/p/pzhnNcFAXGdPfY6jbED71rWqu8gHJelUR5COkK/slide-11.jpg')

@bot.command()
async def news(ctx):
    api_key = '25d347c4b100414293856eb8e3c97263'  
    url = f'https://newsapi.org/v2/everything?q=global%20warming&apiKey={api_key}'
    
    response = requests.get(url)
    news_data = response.json()
    
    if 'articles' in news_data:
        for article in news_data['articles'][:5]:  
            news_title = article['title']
            news_url = article['url']
            await ctx.send(f"**{news_title}**\n{news_url}")
    else:
        await ctx.send('Информация о новостях не найдена')

@bot.command(name='опрос_потепление')
async def опрос_потепление(ctx):
    question = [
        "Как вы оцениваете свои знания о глобальном потеплении? (от 1 до 10)",
        "Считаете ли вы глобальное потепление серьезной проблемой? (Да/Нет)",
        "Что, по вашему мнению, может сделать каждый человек, чтобы снизить влияние глобального потепления?"
        "Что вызывает глобальное потепление?"
        "Какие основные последствия глобального потепления вы можете назвать?"
        "Какие главные газы вызывают парниковый эффект?"
        "Какие регионы наиболее уязвимы к последствиям глобального потепления?"
        "Как можно снизить влияние человеческой деятельности на глобальное потепление?"
        "Какие меры могут помочь адаптироваться к изменению климата?"
        "Какова роль лесов в борьбе с глобальным потеплением?"
         "Какие основные действия планирует принять международное сообщество для сокращения выбросов парниковых газов?"
    ]

    answers = []

    for question in questions:
        await ctx.send(question)
        answer = await bot.wait_for('message')
        answers.append(answer.content)

    await ctx.send("Спасибо за участие в опросе!")
    await ctx.send("Результаты опроса:")
    for i, question in enumerate(questions):
        await ctx.send(f"{question}: {answers[i]}")

@bot.command(name = "помощь")
async def help(ctx):
    await ctx.send("@help - навигация по командам")              
    await ctx.send("@Викторина - запускает викторину по теме: Глобальное потепление")
    await ctx.send("@eco_tips - советы по уменьшению углеродного следа")
    await ctx.send("@show_image - показывает картинку с последствиями от глобального потепления")
    await ctx.send("@news- последние новости по теме глобального потепления")
    await ctx.send("@опрос_потепление - опросник по этой же теме")   


  
@bot.command()
async def climate(ctx):
    info = climate_change_info()
    for key, value in info.items():
        await ctx.send(f"{key}: {value}")

@bot.command()
async def ecochallenge(ctx):
    challenge = random.choice(eco_challenges)
    await ctx.send(f"Вот ваш экологический челлендж: {challenge}")  



def get_weather_info():
    api_key = '4407b7ff1414b7427882c3641feb657e'
    city = 'Novokubansk'
    url = f'https://api.openweathermap.org/data/2.5/weather?lat=45&lon=41&appid=4407b7ff1414b7427882c3641feb657e'
    
    response = requests.get(url)
    data = response.json()
    
    if 'weather' in data and 'main' in data:
        weather_description = data['weather'][0]['description']
        temperature = data['main']['temp']
        return f"Погода в Новокубанске: {weather_description}. Температура: {temperature}°C"
    else:
        return "Информация о погоде недоступна."

@bot.command()
async def send_weather_info(channel):
    weather_info = get_weather_info()
    await channel.send(weather_info)


@bot.command()
async def weather(ctx):
    channel = ctx.channel
    await send_weather_info(channel)   
    
bot.run('Токен не дам, обломитесь')

