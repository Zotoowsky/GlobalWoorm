import asyncio
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


             
bot.run('Токен не дам, обломитесь')

