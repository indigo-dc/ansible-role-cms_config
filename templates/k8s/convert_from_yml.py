import yaml
import json

with open('yaml_referenc/.yml') as f:
    print(json.dumps(yaml.load(f)))
