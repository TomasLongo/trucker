import subprocess
import os
import shutil


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



class Deployment:
    def __init__(self, args):
        self.tool = args['tool']
        self.src = args['source']
        self.dest = args['destination']
        self.script = args['script']

    def exec(self, environ):
        if self.tool == 'cp':
            resolvedSource = os.path.join(environ['WORKDIR'], self.src)
            print(f'copying with cp from {resolvedSource} to {self.dest}')
            shutil.copyfile(resolvedSource, self.dest)
        elif self.tool == 'script':
            process = subprocess.Popen(f"{self.script}", stdout=subprocess.PIPE, shell=True)
            proc_stdout = process.communicate()[0].strip()
            print(proc_stdout)