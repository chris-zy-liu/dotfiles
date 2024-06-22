import subprocess
import sys
import opencc

converter = opencc.OpenCC('t2s.json')
converter.convert('汉字')

process = subprocess.Popen(sys.argv[1:], stdout=subprocess.PIPE)

while True:
    output = process.stdout.readline().decode()
    if output == '' and process.poll() is not None:
        break
    if output:
        print(converter.convert(output.strip()), flush=True)
