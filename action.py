import subprocess

class Action:
    def __init__(self, args):
        self.branchName = args['branch']
        self.repo = args['repo']

    def exec(self):
        process = subprocess.Popen(f"cd /tmp && git clone {self.repo} -b {self.branchName}", stdout=subprocess.PIPE, shell=True)
        proc_stdout = process.communicate()[0].strip()
        print(proc_stdout)


class Build:
    def exec(self):
        process = subprocess.Popen("cd /tmp/notes && ./gradlew build -x test", stdout=subprocess.PIPE, shell=True)
        proc_stdout = process.communicate()[0].strip()
        print(proc_stdout)
