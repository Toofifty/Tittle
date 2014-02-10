import yaml

def load():
    with open('../Tittle/settings.yml', 'r') as conf_file:
        c = yaml.load(conf_file)
    print "!!! - Settings loaded"
    return c