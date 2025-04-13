from . import Notifier
from DesignPatterns.Factory.Email.EmailNotifier import EmailNotifier
from DesignPatterns.Factory.SMS.SMSNotifier import SMSNotifier
from DesignPatterns.Factory.Slack.SlackNotifierAdapter import SlackNotifierAdapter

class NotifierFactory:
    @staticmethod
    def get_notifier(notifier_type: str, **kwargs) -> Notifier:
        match notifier_type.lower():
            case "email":
                return 
            case "sms":
                return SMSNotifier()
            case "slack":
                channel = kwargs.get("channel", "general")
                return SlackNotifierAdapter(channel)
            case _:
                raise ValueError("Unsupported notifier type")