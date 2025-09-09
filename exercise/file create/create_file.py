import os
import yaml
from pathlib import Path

p = Path(".")

print(p)







def create_struture(root,structure):
    print(root,structure)


with open("structure.yml", "r") as f:
    config = yaml.safe_load(f)
    print(config)
    

with open("structure2.yml", "w") as f:
    yaml.safe_dump(config, f)

# print(config)    