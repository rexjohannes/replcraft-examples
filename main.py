from replcraft.main import ReplCraft
import os

client = ReplCraft(os.environ["token"])

client.login()

client.set_block(2, 0, 2, 'minecraft:air')