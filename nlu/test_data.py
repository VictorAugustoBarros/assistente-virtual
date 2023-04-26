import yaml

file = open('/home/victor/git/pessoal/raijin/nlu/train.yml', 'r', encoding="utf-8").read()
commands = yaml.safe_load(file)

for command in commands.get("commands"):
    print(command)
