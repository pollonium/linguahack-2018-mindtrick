import subprocess


class Executor:
    execPath = ''
    configFile = ''

    def __init__(self, config_file='config.proto', exec_path='tomitaparser.exe'):
        self.execPath = exec_path
        self.configFile = config_file

    def execute(self):
        cmd = self.execPath + ' ' + self.configFile
        subprocess.run(cmd)
