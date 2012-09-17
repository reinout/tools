"""
Script to run a command via ssh inside vagrant.

What it does: we're inside a directory that we know has been mounted in a
local vagrant box. We ``cd`` to the corresponding directory and run the
command there.

There are quite some assumptions in here, they match the way I (Reinout) has
set it all up:

- Virtual machines are inside ``~/vm/VM_NAME/``.

- That ``~/vm/VM_NAME/`` directory is mounted as ``/vagrant/`` inside the VM.

- The vm name is "django" for a vm inside ~/vm/django/`` and it has a
  corresponding alias inside your ssh config file. So ssh'ing to "django"
  means you connect just fine to the right VM with the vagrant user. An
  example of such a config that ought to go inside ``~/.ssh/config`` ::

     Host django
         HostName 33.33.33.20
         User vagrant

  Oh, and make sure you use ``ssh-copy-id`` to copy your ssh key to the
  vagrant box, otherwise you'll go mad typing your password all the time.


"""
import os
import sys

from fabric.api import cd
from fabric.api import env
from fabric.api import execute
from fabric.api import run

HOMEDIR = os.path.expanduser('~')
VM_BASEDIR = os.path.join(HOMEDIR, 'vm')
BASEDIR_IN_VAGRANT = '/vagrant/'


def vm_and_path():
    """Return vm name and path inside vm."""
    cur_dir = os.getcwd()
    if not cur_dir.startswith(VM_BASEDIR):
        raise RuntimeError("We're not inside {}".format(VM_BASEDIR))
    remainder = cur_dir.lstrip(VM_BASEDIR)
    parts = remainder.split('/')
    if not parts:
        raise RuntimeError("We're not inside {}/VM_NAME".format(VM_BASEDIR))
    vm_name = parts[0]
    vagrant_path = BASEDIR_IN_VAGRANT + '/'.join(parts[1:])
    return vm_name, vagrant_path


def run_cmd():
    with cd(env.my_path):
        run(env.my_cmd)


def main():
    env.use_ssh_config = True
    vm_name, path = vm_and_path()
    cmd = ' '.join(sys.argv[1:])
    env.hosts = [vm_name]
    env.my_cmd = cmd
    env.my_path = path
    execute(run_cmd)
