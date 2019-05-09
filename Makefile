install:
	pipx install --spec . -e tools
	./install_shell_scripts.sh
	python3 generate_python_docs.py
	python3 generate_shell_docs.py
