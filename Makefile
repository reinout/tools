usage:
	echo "make linux or make osx, please"


osx: osx-deps install osx-checkoutmanager local-dev

linux: linux-deps readlinehack install linux-checkoutmanager local-dev

osx-deps:
	brew update
	brew upgrade
	brew install \
	ack \
	entr \
	npm \
	pipx \
	shellcheck \
	the_silver_searcher \
	tidy-html5
	pipx reinstall-all

linux-deps:
	sudo aptitude install \
	ack \
	entr \
	npm \
	pipx \
	shellcheck \
	silversearcher-ag \
	tidy


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
	   ~/.local/pipx/venvs/flake8\
	   ~/.local/pipx/venvs/isort\
	   ~/.local/pipx/venvs/legit\
	   ~/.local/pipx/venvs/oplop\
	   ~/.local/pipx/venvs/pipenv\
	   ~/.local/pipx/venvs/pre-commit\
	   ~/.local/pipx/venvs/tox


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
	cd /tmp && pipx install --force --editable ~/zelf/tools && cd -
	./install_shell_scripts.sh
	python3 generate_python_docs.py
	python3 generate_shell_docs.py


local-dev:
	checkoutmanager co
	pipx install --force --editable ~/opensource/checkoutmanager
	pipx install --force --editable ~/opensource/zest.releaser
	pipx install --force --editable ~/opensource/z3c.dependencychecker
	pip3 install flake8
