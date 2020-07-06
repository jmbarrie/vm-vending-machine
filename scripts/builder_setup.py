"""
This script is used in conjunction with the builder_merge.py script. It utilizes the builders.template.json file and
populates with specified VM configuration items such as vm_name, memory, cpu, and disk_size.

NOTE: This script may be expanded to include other variables but the command line arguments section will be updated to
reflect this.

Command line arguments: {{ os_family }} {{ vm_name }} {{ memory }} {{ cpu_num }} {{ disk_size }}
"""

import sys

vm_name = sys.argv[2]
memory = sys.argv[3]
cpu_num = sys.argv[4]
disk_size = sys.argv[5]
pwd = sys.argv[6]

builder_file = 'templates/builders.template.json'
output_file = f"{sys.argv[1]}/builders/{vm_name}_builder.json"

templated_items = ['<VM_NAME>', '<CPU_NUM>', '<MEMORY>', '<DISK_SIZE>', '<PWD>']
templated_values = [vm_name, cpu_num, memory, disk_size, pwd]

with open(builder_file, 'r') as template_file:
    template_data = template_file.read()

replace_data = template_data

for item, value in zip(templated_items, templated_values):
    replace_data = replace_data.replace(item, value)

with open(output_file, 'w') as write_file:
    write_file.write(replace_data)

