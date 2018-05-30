install:
	pipsi upgrade -e . || true
	./install_shell_scripts.sh
