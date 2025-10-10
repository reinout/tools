doc:
	@echo make install: install everything, including ourselves
	@echo make upgrade: update/upgrade uv, brew, uv tool
	@echo make ourselves: generate docs and install ourselves


install: osx-deps ourselves uv-tools local-dev npm


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
	gdal \
	git-annex \
	git-lfs \
	gpg \
	graphviz \
	hadolint \
	helm \
	htop \
	imagemagick \
	jq \
	just \
	kicad \
	languagetool \
	ltex-ls-plus \
	mactex-no-gui \
	mc \
	nmap \
	npm \
	odt2txt \
	orbstack \
	pgadmin4 \
	pinentry-mac \
	pre-commit \
	pulumi/tap/pulumi \
	pv \
	python@3.12 \
	python@3.13 \
	rg \
	siderolabs/tap/omnictl \
	siderolabs/tap/sidero-tools \
	siderolabs/tap/talosctl \
	sops \
	spatialite-tools \
	starship \
	tectonic \
	terraform \
	texlab \
	tidy-html5 \
	tree \
	watch \
	wget \
	wine-stable


uv-tools: ~/.local/share/uv/tools/ansible\
	  ~/.local/share/uv/tools/ansible-lint\
	  ~/.local/share/uv/tools/beautysh\
	  ~/.local/share/uv/tools/cookiecutter\
	  ~/.local/share/uv/tools/docutils\
	  ~/.local/share/uv/tools/dotfiles\
	  ~/.local/share/uv/tools/legit\
	  ~/.local/share/uv/tools/oplop\
	  ~/.local/share/uv/tools/pyright\
	  ~/.local/share/uv/tools/pyupgrade\
	  ~/.local/share/uv/tools/tox \
	  ~/.local/share/uv/tools/ty

~/.local/share/uv/tools/ansible:
	uv tool install --with-executables-from ansible-core,ansible-lint ansible


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


ourselves: /Users/reinout/.cargo/bin/uv ~/Dotfiles
	./install_shell_scripts.sh
	uv tool install --editable .
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
