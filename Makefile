usage:
	echo "make linux or make osx, please"


osx: osx-deps install osx-checkoutmanager local-dev

linux: linux-deps readlinehack install linux-checkoutmanager local-dev

osx-deps:
	brew install \
	ack \
	entr \
	npm \
	pipx \
	shellcheck \
	the_silver_searcher \
	tidy-html5

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


pyenv: ~/.pyenv ~/.pyenv/versions/2.7.15 ~/.pyenv/versions/3.5.6 ~/.pyenv/versions/3.6.5 ~/.pyenv/versions/3.7.3 pyenv-activate

~/.pyenv:
	curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash

~/.pyenv/versions/%:
	pyenv install $*

pyenv-activate:
	pyenv global 3.7.3 3.6.5 3.5.6

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

install: pipx-deps pyenv ~/Dotfiles npm-deps
	cd .. && pipx install --force --editable tools && cd tools
	./install_shell_scripts.sh
	python3 generate_python_docs.py
	python3 generate_shell_docs.py


local-dev:
	checkoutmanager co
	pipx install --force --editable --spec ~/opensource/checkoutmanager checkoutmanager
	pipx install --force --editable --spec ~/opensource/zest.releaser zest.releaser
	pipx install --force --editable --spec ~/opensource/z3c.dependencychecker z3c.dependencychecker
	pip3 install flake8
