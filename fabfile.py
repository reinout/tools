from fabric.api import cd
from fabric.api import env
from fabric.api import run
from fabric.api import sudo
from fabric.contrib.files import exists


env.forward_agent = True


def vmware_bootstrap():
    """Bootstrap my setup on vmware."""
    if not exists("~/Dotfiles"):
        sudo("aptitude install git -y")
        run("git clone ssh://vanrees.org/~/repos/Dotfiles")
    if not exists("~/tools"):
        run("git clone git@github.com:reinout/tools.git")
    if not exists("~/utils"):
        run("ln -s /mnt/hgfs/reinout/utils utils")
    with cd("~/tools"):
        if not exists("buildout.cfg"):
            run("ln -s vmware.cfg buildout.cfg")
        run("python bootstrap.py")
        run("bin/buildout")
