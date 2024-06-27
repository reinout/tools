# 'osx' is the default install-everything target, 'install' installs
# ourselves.
install: osx-deps npm ourselves_install local-dev extra-pipx


upgrade:
	brew update
	brew upgrade
	pipx reinstall-all


osx-deps:
	brew update
	brew install \
	ag \
	age \
	arduino-cli \
	awscli \
	bash-completion@2 \
	fd \
	ffmpeg \
	gpg \
	graphviz \
	hadolint \
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
	tectonic \
	terraform \
	texlab \
	tree \
	watch \
	wget \
	tidy-html5
	@echo "================================================================================="
	@echo "A 'pipx reinstall-all' might be needed if there was a brew python version upgrade"
	@echo "================================================================================="
	cd /tmp && pipx install --force --editable ~/zelf/tools && cd -


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
	   ~/.local/pipx/venvs/mopup \
	   ~/.local/pipx/venvs/oplop\
	   ~/.local/pipx/venvs/pipenv\
	   ~/.local/pipx/venvs/pyupgrade\
	   ~/.local/pipx/venvs/tox \
	   ~/.local/pipx/venvs/uv \
	   ~/.local/pipx/venvs/youtube-dl


~/.local/pipx/venvs/ansible:
	pipx install --include-deps ansible --pip-args dnspython


~/.local/pipx/venvs/%:
	pipx install $*


~/Dotfiles:
	cd ~ && git clone ssh://vanrees.org/~/repos/Dotfiles
	dotfiles --sync
	echo "You might want to run dotfiles --sync --force, btw"


ourselves_install: pipx-deps ~/Dotfiles
	./install_shell_scripts.sh
	python3 generate_python_docs.py
	python3 generate_shell_docs.py


local-dev:
	checkoutmanager co
	pipx install --force --editable ~/opensource/checkoutmanager
	pipx install --force --editable ~/opensource/zest.releaser
	pipx install --force --editable ~/opensource/z3c.dependencychecker
	pipx install --force --editable ~/zelf/denoter


extra-pipx:
	pipx inject tox tox-uv
	pipx inject --editable zest.releaser ~/opensource/qgispluginreleaser


npm:
	npm install -g @mermaid-js/mermaid-cli
