
import discord
import openai

# Set up the OpenAI API key
openai.api_key = "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"
# Create a new Discord client
#client = discord.Client(intents=discord.Intents.default())

#TypeError: __init__() missing 1 required keyword-only argument: 'intents'

client = discord.Client(intents=discord.Intents.all())


@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')
@client.event


async def on_message(message):
    if message.author == client.user:
        return

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt= message.content,
        temperature=0.75,
        max_tokens=4000,
        
        
    )

    
    #print(response)
    #print(message.content)

    await message.channel.send(response['choices'][0]['text'])
    



# Run the Discord client
client.run("MTA0OTkzMjk3MTg3MzkyNzE4OA.GyZgaV.cspoZ_UaQO1EfB_Y79jlLyQBuwFGw5tgO8lWYo")
