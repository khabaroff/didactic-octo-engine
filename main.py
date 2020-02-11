import config
import telebot
from aiohttp import web
import ssl

bot = telebot.TeleBot(config.token)

# Echo handler
@bot.message_handler(content_types=['text'])
def handle_text(message):
    bot.send_message(message.chat.id, message.text)


# Handle data from webhook
async def webhook_handle(request):
    if request.path.replace('/', '') == bot.token:
        request_body_dict = await request.json()
        update = telebot.types.Update.de_json(request_body_dict)
        bot.process_new_updates([update])
        return web.Response()
    else:
        return web.Response(status=403)


# Setup webhook
def webhook_setup():
    webhook_url_base = f'https://{config.host}:{config.port}'
    webhook_url_path = f'/{config.token}/'

    app = web.Application()
    app.router.add_post(webhook_url_path, webhook_handle)

    bot.remove_webhook()
    bot.set_webhook(url=webhook_url_base + webhook_url_path, certificate=open(config.cert, 'r'))

    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    context.load_cert_chain(config.cert, config.pkey)

    web.run_app(
        app,
        host=config.listen,
        port=config.port,
        ssl_context=context
    )


if __name__ == '__main__':
    setup_webhook()