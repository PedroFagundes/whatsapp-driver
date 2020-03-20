import os
import sys
import time
import requests

from webwhatsapi import WhatsAPIDriver
from webwhatsapi.objects.chat import GroupChat, Chat


def run():
    print("Environment", os.environ)
    # try:
    #     os.environ["SELENIUM"]
    # except KeyError:
    #     print("Please set the environment variable SELENIUM to Selenium URL")
    #     sys.exit(1)

    driver = WhatsAPIDriver(
        username='sorrisus', loadstyles=True,
        profile='/home/livelabs01/Development/WebWhatsapp-Wrapper/profile')
    print("Waiting for QR")
    driver.wait_for_login()
    driver.save_firefox_profile(remove_old=True)
    print("Bot started")

    # Answering to unread messages
    # unread_messages = driver.get_unread(include_notifications=True)

    # for chat_messages in unread_messages:
    #     if not isinstance(chat_messages.chat, GroupChat):
    #         last_message = chat_messages.messages[-1]
    #         if last_message.type in ['chat']:
    #             answers = requests.post(
    #                 'http://sorrisus.localhost:8000/api/v1/answer',
    #                 json={'sentence': message.content})

    #             for answer in answers.json():
    #                 driver.send_message_to_id(
    #                     last_message.sender.id, answer.get('sentence'))

    driver.subscribe_new_messages(NewMessageObserver(driver))
    print("Waiting for new messages...")

    """ Locks the main thread while the subscription in running """
    while True:
        time.sleep(60)


class NewMessageObserver():

    def __init__(self, driver, *args, **kwargs):
        if not driver:
            print("Driver not informed")
            sys.exit(1)
        self.driver = driver
        super(NewMessageObserver, self).__init__(*args, **kwargs)

    def on_message_received(self, new_messages):
        for message in new_messages:
            if message.type == 'chat':
                print("New message '{}' received from number {}".format(
                    message.content, message.sender.id))

                message_chat = self.driver.get_chat_from_id(message.chat_id)

                if not isinstance(message_chat, GroupChat):
                    if message.type in ['chat']:
                        # self.driver.send_message_to_id(
                        # message.sender.id,
                        # '🤖 - Estou em manutenção. Já já estou de volta')
                        answers = requests.post(
                            'http://sorrisus.localhost:8000/api/v1/answer',
                            json={'sentence': message.content})

                        for answer in answers.json():
                            self.driver.send_message_to_id(
                                message.sender.id, answer.get('sentence'))
            else:
                self.driver.send_message_to_id(
                    message.sender.id, '🤖 - Ainda não entendo mensagens desse \
                        tipo 😔\n\nMas tranquilo! Creio que meus criadores já \
                        estão trabalhando em uma forma de me ensinar ☺')
                print(
                    "New message of type '{}' received from number {}".format(
                        message.type, message.sender.id))

        # Set message as seen
        self.driver.chat_send_seen(message.chat_id)


if __name__ == '__main__':
    run()
