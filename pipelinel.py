import yaml
import action as BuildActions

class Pipeline:
    def readPipeline(self, name):
        with open("/Users/tlongo/projects/python/trucker/resources/pipeline.yml") as stream:
            self.pipline = yaml.load(stream)['pipeline']

        actions = self.pipline['actions']
        self.actions = []
        for action in actions:
            if action['type'] == 'checkout':
                foundAction = BuildActions.Action(action)
                self.actions.append(foundAction)



    def name(self):
        return self.pipline['name']

    def run(self):
        for action in self.actions:
            action.exec()

    def __str__(self):
        return self.pipline.__str__()


def createAction(type, args):
    if type == 'checkout':
        foundAction = BuildActions.Action(args)


