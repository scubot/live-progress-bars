import discord
import tqdm
import time
from modules.botModule import BotModule
import sys, os


class LiveProgressBars(BotModule):
    name = 'liveprogressbar'

    description = 'Experimental live progress bar'

    help_text = '`!progressbar` - try it out'

    trigger_string = 'progressbar'

    async def parse_command(self, message, client):
        # First, we make a new progress bar object.
        pb = tqdm.tqdm(total=10, mininterval=2, file=open(os.devnull, 'w'))
        message_r = await client.send_message(message.channel, pb)
        for x in range(10):
            time.sleep(3)
            # Then, we can update it whenever we want (incrementing)
            pb.update(1)
            await client.edit_message(message_r, pb)
        # Remember to close!
        pb.close()


