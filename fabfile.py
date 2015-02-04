from fabric.api import cd
from fabric.api import env
from fabric.api import run
from fabric.api import sudo
from fabric.contrib.files import exists

env.forward_agent = True


def vmware_bootstrap():
    """Bootstrap my setup on vmware."""
    sudo("aptitude install git python-dev ncurses-dev build-essential -y")
    # ^^^ Git is needed for checkouts, python-dev and ncursus-dev for
    # compiling several python packages we want to install.
    if not exists("~/Dotfiles"):
        run("git clone ssh://vanrees.org/~/repos/Dotfiles")
    if not exists("~/tools"):
        run("git clone git@github.com:reinout/tools.git")
    if not exists("~/utils"):
        run("ln -s /mnt/hgfs/reinout/utils utils")

    # Create a /Users symlink to /home: this helps with the buildout default
    # config file that doesn't do tilde expansion.
    if not exists("/Users"):
        sudo("ln -s /home /Users")
    run("mkdir -p ~/.buildout/eggs")
    run("mkdir -p ~/.buildout/downloads")
    run("mkdir -p ~/.buildout/configs")

    with cd("~/tools"):
        run("git pull")
        if not exists("buildout.cfg"):
            run("ln -s vmware.cfg buildout.cfg")
        run("python bootstrap.py")
        run("bin/buildout")
        run("./install_shell_scripts.sh")
    with cd("~/Dotfiles"):
        run("git pull")
    run("~/tools/bin/dotfiles --sync --force")

    if not exists("~/%s" % env.host):
        run("ln -s /mnt/hgfs/reinout/%s %s" % (env.host, env.host))

# TODO: vmware setup (build-essentials, vmware tools, mount options.

# TODO: hostname in the vm, hostname in our local /etc/hosts, hostname in the
# ssh config
