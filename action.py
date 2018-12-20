import subprocess
import os


class Action:
    def __init__(self, args):
        self.branchName = args['branch']
        self.repo = args['repo']

    def exec(self, environ):
        buildRepo = os.path.join(environ['WORKDIR'], os.path.basename(self.repo))
        print(f"Buildrepo {buildRepo}")
        environ['BUILDREPO'] = buildRepo
        process = subprocess.Popen(f"cd {environ['WORKDIR']} && git clone {self.repo} -b {self.branchName}", stdout=subprocess.PIPE, shell=True)
        proc_stdout = process.communicate()[0].strip()
        print(proc_stdout)


class Build:
    def __init__(self, args):
        self.command = args['command']

    def exec(self, environ):
        process = subprocess.Popen(f"cd {environ['BUILDREPO']} && {self.command}", stdout=subprocess.PIPE, shell=True)
        proc_stdout = process.communicate()[0].strip()
        print(proc_stdout)
