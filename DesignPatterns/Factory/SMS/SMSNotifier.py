from DesignPatterns.Factory.Notifier import Notifier

class SMSNotifier(Notifier):
    def send(self, message: str) -> None:
        print(f"SMS: {message}")
    