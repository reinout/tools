doc:
	@echo make install: install everything, including ourselves
	@echo make upgrade: update/upgrade uv, brew, uv tool


install: osx-deps ourselves_install uv-tools local-dev npm


upgrade:
	uv self update
	uv tool upgrade --all
	uv cache prune
	brew update
	brew upgrade


osx-deps:
	brew update
	brew install \
	ag \
	age \
	arduino-cli \
	awscli \
	bash-completion@2 \
	bat \
	direnv \
	fd \
	ffmpeg \
	git-annex \
	git-lfs \
	gpg \
	graphviz \
	hadolint \
	htop \
	imagemagick \
	just \
	jq \
	kicad \
	mactex-no-gui \
	mc \
	npm \
	odt2txt \
	orbstack \
	pinentry-mac \
	pulumi/tap/pulumi \
	pre-commit \
	pv \
	python@3.12 \
	python@3.13 \
	rg \
	siderolabs/tap/sidero-tools \
	starship \
	tectonic \
	terraform \
	texlab \
	tree \
	watch \
	wget \
	tidy-html5


uv-tools: ~/.local/share/uv/tools/ansible\
	  ~/.local/share/uv/tools/ansible-lint\
	  ~/.local/share/uv/tools/beautysh\
	  ~/.local/share/uv/tools/black\
	  ~/.local/share/uv/tools/cookiecutter\
	  ~/.local/share/uv/tools/docutils\
	  ~/.local/share/uv/tools/dotfiles\
	  ~/.local/share/uv/tools/flake8\
	  ~/.local/share/uv/tools/isort\
	  ~/.local/share/uv/tools/legit\
	  ~/.local/share/uv/tools/oplop\
	  ~/.local/share/uv/tools/pyright\
	  ~/.local/share/uv/tools/pyupgrade\
	  ~/.local/share/uv/tools/tox \
	  ~/.local/share/uv/tools/ty \
	  ~/.local/share/uv/tools/youtube-dl


~/.local/share/uv/tools/ansible:
	uv tool install --with-executables-from ansible-core,ansible-lint ansible
	# uv tool install ansible-core --with dnspython --with ansible


~/.local/share/uv/tools/tox:
	uv tool install tox --with tox-uv


~/.local/share/uv/tools/%:
	uv tool install $*


~/Dotfiles:
	cd ~ && git clone ssh://vanrees.org/~/repos/Dotfiles
	uvx dotfiles --sync
	echo "You might want to run dotfiles --sync --force, btw"


/Users/reinout/.cargo/bin/uv:
	curl -LsSf https://astral.sh/uv/install.sh | sh


ourselves_install: /Users/reinout/.cargo/bin/uv ~/Dotfiles
	./install_shell_scripts.sh
	uv tool install .
	uv run ./generate_python_docs.py
	uv run ./generate_shell_docs.py


local-dev:
	uvx checkoutmanager co
	uv tool install --editable ~/opensource/zest.releaser/ --with ~/opensource/qgispluginreleaser
	uv tool install --editable ~/opensource/checkoutmanager/
	uv tool install --editable ~/zelf/denoter/
	uv tool install --editable ~/nens/nens-meta/


npm:
	npm install -g @mermaid-js/mermaid-cli
