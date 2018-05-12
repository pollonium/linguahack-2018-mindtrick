import subprocess
import sys


class Executor:
    execPath = 'tomitaparser.exe'
    configFile = 'config.proto'
    prevFilename = '26_4.txt'

    def execute(self, filename):
        file = open(self.configFile, 'r', encoding='utf-8')
        config = file.read()
        file.close()
        file = open(self.configFile, 'w', encoding='utf-8')
        config.replace(self.prevFilename, filename)
        file.write(config)
        self.prevFilename = filename
        cmd = self.execPath + ' ' + self.configFile
        print(cmd)
        subprocess.run(cmd)
