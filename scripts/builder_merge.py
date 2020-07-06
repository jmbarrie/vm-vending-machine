"""
This script is used in conjunction with the builder_setup.py script. It will take the produced {vm_name}_builder.json
files and will merge then. It will then fill in the Packer template at the <BUILDERS> section.

The outcome of this should allow for utilizing Packer's parallel processing functions.

Command line arguments: {{ os_family }} {{ os_name }} {{ build_version }} {{ vm_name|join(' ') }}
"""

import sys
from os import path

os_family = sys.argv[1]
os_name = sys.argv[2]
build_version = sys.argv[3]

packer_template_file = f"{os_family}/{os_name}.template.json"
merged_packer_file = f"{os_family}/{os_name}_packer_{build_version}.json"

data = []

for vm_name in sys.argv[3:]:
    template_file = f"{sys.argv[1]}/builders/{vm_name}_builder.json"
    if path.isfile(template_file):
        with open(template_file, 'r') as builder_file:
            data.append(builder_file.read())

merged_builder_data = ",\n".join(data)

with open(packer_template_file, 'r') as file:
    template_data = file.read()

merged_template_data = template_data.replace('<BUILDER>', merged_builder_data)

with open(merged_packer_file, 'w') as file:
    file.write(merged_template_data)

