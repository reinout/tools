usage:
	echo "make linux or make osx, please"


osx: osx-deps install osx-checkoutmanager local-dev

linux: linux-deps readlinehack install linux-checkoutmanager local-dev

osx-deps: /usr/local/bin/pipx \
	  /usr/local/bin/shellcheck \
	  /usr/local/bin/npm \
	  /usr/local/bin/tidy

linux-deps: /usr/bin/pipx \
	    /usr/bin/shellcheck \
	    /usr/bin/npm \
	    /usr/bin/tidy


/usr/bin/%:
	sudo aptitude install $*

/usr/local/bin/%:
	brew install %*


readlinehack: /lib/x86_64-linux-gnu/libreadline.so.7
	sudo pip3 install readline

/lib/x86_64-linux-gnu/libreadline.so.7:
	sudo ln -s /lib/x86_64-linux-gnu/libreadline.so.8 $@

pipx-deps: ~/.local/pipx/venvs/ansible\
	   ~/.local/pipx/venvs/cookiecutter\
	   ~/.local/pipx/venvs/docutils\
	   ~/.local/pipx/venvs/flake8\
	   ~/.local/pipx/venvs/isort\
	   ~/.local/pipx/venvs/legit\
	   ~/.local/pipx/venvs/oplop\
	   ~/.local/pipx/venvs/dotfiles\
	   ~/.local/pipx/venvs/checkoutmanager\
	   ~/.local/pipx/venvs/pipenv


~/.local/pipx/venvs/%:
	pipx install $*


pyenv: ~/.pyenv ~/.pyenv/versions/2.7.15 ~/.pyenv/versions/3.5.6 ~/.pyenv/versions/3.6.5 ~/.pyenv/versions/3.7.3

~/.pyenv:
	curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash

~/.pyenv/versions/%:
	pyenv install $*


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


install: pipx-deps pyenv ~/Dotfiles npm-deps
	pipx install --force --editable --spec . tools
	./install_shell_scripts.sh
	python3 generate_python_docs.py
	python3 generate_shell_docs.py


local-dev:
	checkoutmanager co
	pipx install --force --editable --spec ~/opensource/checkoutmanager checkoutmanager
	pipx install --force --editable --spec ~/opensource/zest.releaser zest.releaser
	pipx install --force --editable --spec ~/opensource/z3c.dependencychecker z3c.dependencychecker
	pip3 install flake8
