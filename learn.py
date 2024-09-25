from glob import glob
from aiml import Kernel


k = Kernel()
aiml_files = glob('C:/Users/MUHAMMAD HASEEB/Documents/CHATBOT/Easy-Chatbot-master/data/*.aiml')

for file_path in aiml_files:
    k.learn(file_path)

