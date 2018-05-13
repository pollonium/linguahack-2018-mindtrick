import subprocess


class Executor:
    execPath = 'tomitaparser.exe'
    configFile = 'config.proto'
    prevFilename = '9_9.txt'

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
