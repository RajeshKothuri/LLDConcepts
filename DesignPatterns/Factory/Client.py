from .NotifierFactory import NotifierFactory

if __name__ == "__main__":
    notifier_type = input("Enter notifier type (email/sms/slack): ")
    channel = input("Enter channel name for slack: ")
    notifier = NotifierFactory.get_notifier(notifier_type, channel = channel)
    notifier.send("Testing Notification Service")