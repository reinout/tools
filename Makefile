usage:
	echo "make linux or make osx, please"


osx: osx-deps install osx-checkoutmanager local-dev-osx

linux: linux-deps readlinehack install linux-checkoutmanager local-dev-linux

osx-deps:
	brew update
	brew upgrade
	brew install \
	ag \
	awscli \
	bash-completion@2 \
	fd \
	ffmpeg \
	gpg \
	hadolint \
	pinentry-mac \
	htop \
	imagemagick \
	jq \
	mactex-no-gui \
	mc \
	npm \
	odt2txt \
	pinentry-mac \
	pipx \
	pre-commit \
	pv \
	rg \
	terraform \
	tree \
	watch \
	wget \
	youtube-dl \
	tidy-html5
	cd /tmp && pipx install --force --editable ~/zelf/tools && cd -
#	pipx reinstall-all

linux-deps:
	sudo aptitude install \
	ack \
	entr \
	npm \
	pipx \
	python3-venv \
	shellcheck \
	silversearcher-ag \
	tidy
	cd /tmp && pipx install --spec ~/zelf/tools --force --editable tools && cd -


readlinehack: /lib/x86_64-linux-gnu/libreadline.so.7
	sudo pip3 install readline

/lib/x86_64-linux-gnu/libreadline.so.7:
	sudo ln -s /lib/x86_64-linux-gnu/libreadline.so.8 $@

pipx-deps: ~/.local/pipx/venvs/ansible\
	   ~/.local/pipx/venvs/ansible-lint\
	   ~/.local/pipx/venvs/beautysh\
	   ~/.local/pipx/venvs/black\
	   ~/.local/pipx/venvs/checkoutmanager\
	   ~/.local/pipx/venvs/cookiecutter\
	   ~/.local/pipx/venvs/docutils\
	   ~/.local/pipx/venvs/dotfiles\
	   ~/.local/pipx/venvs/pipenv\
	   ~/.local/pipx/venvs/pyupgrade\
	   ~/.local/pipx/venvs/flake8\
	   ~/.local/pipx/venvs/isort\
	   ~/.local/pipx/venvs/legit\
	   ~/.local/pipx/venvs/oplop\
	   ~/.local/pipx/venvs/tox


~/.local/pipx/venvs/ansible:
	pipx install --include-deps ansible --pip-args dnspython

~/.local/pipx/venvs/%:
	pipx install $*

osx-checkoutmanager: ~/.checkoutmanager.cfg ~/.checkoutmanager_osx.cfg
	ln -sf ~/.checkoutmanager_osx.cfg ~/.checkoutmanager.cfg

linux-checkoutmanager: ~/.checkoutmanager.cfg ~/.checkoutmanager_linux.cfg
	ln -sf ~/.checkoutmanager_linux.cfg ~/.checkoutmanager.cfg


~/Dotfiles:
	cd ~ && git clone ssh://vanrees.org/~/repos/Dotfiles
	dotfiles --sync
	echo "You might want to run dotfiles --sync --force, btw"


npm-deps: ~/Dotfiles ~/.npm-packages \
		~/.npm-packages/bin/js-yaml \
		~/.npm-packages/bin/csslint \
		~/.npm-packages/bin/jshint

~/.npm-packages:
	mkdir $@

~/.npm-packages/bin/%:
	npm install -g $*


# pipx install --force --editable --spec . tools

install: pipx-deps ~/Dotfiles npm-deps
	./install_shell_scripts.sh
	python3 generate_python_docs.py
	python3 generate_shell_docs.py


local-dev-osx:
	checkoutmanager co
	pipx install --force --editable ~/opensource/checkoutmanager
	pipx install --force --editable ~/opensource/zest.releaser
	pipx install --force --editable ~/opensource/z3c.dependencychecker
	pip3 install flake8

local-dev-linux:
	checkoutmanager co
	pipx install --spec ~/opensource/checkoutmanager --force --editable checkoutmanager
	pipx install --spec ~/opensource/zest.releaser --force --editable zest.releaser
	pipx install --spec ~/opensource/z3c.dependencychecker --force --editable z3c.dependencychecker
	pip3 install flake8
