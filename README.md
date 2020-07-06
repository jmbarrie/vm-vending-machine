# VM Vending Machine

### General 
VM Vending Machine is an open source VM creation tool utilizing Ansible and Packer. This tool is currently utilized to
produce CentOS 7 VirtualBox golden images, but will be expanded to include various Linux and Windows operating systems.
Playbooks and templates are a work in progress, and will be updated as development continues. In its current state, the
Vending Machine processes Packer files in serial, but the intended outcome is to introduce a parallel solution.

### VM Vending

#### Dependencies
Vending Machine is intended to be used with the following tools:
- Packer
- Ansible
- Python 3.6+
- VirtualBox

#### Example usage

The current iteration of the Vending Machine is set up to be plug and play. Navigate to the project's root directory and
run `playbook.yml`.

```
$ cd vm-vending-machine
$ ansible-playbook playbook.yml
```

The default settings can be adjusted in the `vars/vars.yml` file under the `Config Variables` section:
- VM Name: TestVM1
- VM Memory: 512 MB
- VM CPU Cores: 1
- VM Disk Size: 10240

Aside from installing Ansible on the images, there is currently no other changes to the base CentOS 7 Minimal ISO.

NOTE: The Packer template is currently implemented to search for the CentOS ISO in the `packer_templates/centos/`
directory, but this can be adjusted in the `builders.template.json` file. This will change as supported ISO's are 
implemented.
