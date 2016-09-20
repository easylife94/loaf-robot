import aiml
import os
alice = aiml.Kernel()

if os.path.isfile("bot_brain.brn"):
    alice.bootstrap(brainFile="bot_brain.brn")
else:
    alice.bootstrap(learnFiles="std-startup.xml", commands="LOAD ALICE")
    alice.saveBrain("bot_brain.brn")

while(True):
    print alice.respond(raw_input(">> "))