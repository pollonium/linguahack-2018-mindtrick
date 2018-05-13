import subprocess


class Executor:
    execPath = ''
    configFile = ''
    prevFilename = ''

    def __init__(self, prev_filename, config_file='config.proto', exec_path='tomitaparser.exe'):
        self.prevFilename = prev_filename
        self.execPath = exec_path
        self.configFile = config_file

    def execute(self, filename):
        file = open(self.configFile, 'r', encoding='utf-8')
        config = file.read()
        file.close()
        config = config.replace(self.prevFilename, filename)
        file = open(self.configFile, 'w', encoding='utf-8')
        file.write(config)
        file.close()
        self.prevFilename = filename
        cmd = self.execPath + ' ' + self.configFile
        subprocess.run(cmd)
