from DesignPatterns.Factory.Notifier import Notifier

class EmailNotifier(Notifier):
    def send(self, message: str) -> None:
        print(f"Email: {message}")
    