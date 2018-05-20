install:
	pipsi install -e . || true
	./install_shell_scripts.sh
