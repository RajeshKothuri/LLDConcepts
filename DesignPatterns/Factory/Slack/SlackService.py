class SlackService:
    def post_to_channel(self, channel: str, content: str) -> None:
        print(f"posting to slack channel #{channel}: {content}")