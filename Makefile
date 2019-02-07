install:
	pipsi upgrade -e . || true
	./install_shell_scripts.sh
	python3 generate_python_docs.py
	python3 generate_shell_docs.py
