import time

from codeborn_client.bot import Bot
from codeborn_client.messages import ApiMessage, MessageType


class NoopBot(Bot):
    """A bot that does nothing except respond to heartbeats."""

    def run(self) -> None:

        message = ApiMessage(
            type=MessageType.command,
            payload={
                'command': 'merge',
                'armies': [str(army['gid']) for army in self.game_state['me']['armies']]
            }
        )
        self.send(message)

        while True:
            time.sleep(5)


if __name__ == '__main__':
    NoopBot().start()
