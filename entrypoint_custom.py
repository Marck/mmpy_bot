from mmpy_bot import Bot, Settings, ExamplePlugin, WebHookExample
# from my_plugin import MyPlugin  <== Example of importing your own plugin, don't forget to add it to the plugins list.

bot = Bot(
    settings=Settings(
        #MATTERMOST_URL = "https://mattermost-team-edition-cog-innovatie-mattermost-bot-marc.apps.ml02.chp.belastingdienst.nl",
	MATTERMOST_URL = 'http://mattermost-cog-innovatie-mattermost-bot-marc-test/',
        #MATTERMOST_PORT = 443,
        BOT_TOKEN = 'so6tf744pfbtipuxetdupb4gqe',
        BOT_TEAM = "im",
        SSL_VERIFY = False,
    	DEBUG = True,
    	RESPOND_CHANNEL_HELP = True
    )
)
bot.run()
