import yaml
import action as BuildActions
import os
import base64
import datetime
import uuid


class Pipeline:

    def __init__(self):
        self.environ = {}
        self.truckerDir = os.path.join(os.environ['HOME'], ".trucker")
        self.createTruckerDirIfNecessary()
        self.actions = []
        self.pipeline = {}

    def readPipeline(self, name):
        with open(os.path.join(os.getcwd(), "pipeline.yml")) as stream:
            self.pipeline = yaml.load(stream)['pipeline']

        actions = self.pipeline['actions']
        self.actions = []
        for action in actions:
            self.actions.append(createAction(action['type'], action))

    def createTruckerDirIfNecessary(self):
        if not os.path.exists(self.truckerDir):
            os.mkdir(self.truckerDir)

    def name(self):
        return self.pipeline['name']

    def run(self):
        # create pipeline working directory
        buildpath = os.path.join(self.truckerDir, self.pipeline['name'], self.createWorkdingDirName())
        os.makedirs(buildpath)
        self.environ['WORKDIR'] = buildpath
        for action in self.actions:
            action.exec(self.environ)

    def __str__(self):
        return self.pipeline.__str__()

    def createWorkdingDirName(self):
        return uuid.uuid4().__str__()

    def printEnviron(self):
        print(self.environ)

def createAction(type, args):
    if type == 'checkout':
        return BuildActions.Action(args)
    elif type == 'build':
        return BuildActions.Build(args)
    elif type == 'deploy':
        return BuildActions.Deployment(args)

