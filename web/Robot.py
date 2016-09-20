import aiml
import os

class Robot:
    def __init__(self):
        self.alice = aiml.Kernel()
        if os.path.isfile("bot_brain.brn"):
            self.alice.bootstrap(brainFile="bot_brain.brn")
        else:
            self.alice.bootstrap(learnFiles="robot-startup.xml", commands="LOAD ALICE")
            self.alice.saveBrain("bot_brain.brn")
    def respond(self,req):
        return self.alice.respond(req)