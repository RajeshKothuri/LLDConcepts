from DesignPatterns.Factory.Notifier import Notifier
from .SlackService import SlackService

class SlackNotifierAdapter(Notifier):
    def __init__(self, channel):
        self.slack = SlackService()
        self.channel = channel

    def send(self, message: str) -> None:
        self.slack.post_to_channel(self.channel, message)
        
