from aiml import Kernel
from glob import glob


# instanciating
bot = Kernel()


# infinite loop for bot
# while True:
#     response = bot.respond(input("> "), 'user1')

#     result = check_predicates()
#     if result:
#         response = result

#     print(response)
#     print()
#     if response.lower() == 'bye':
#         break