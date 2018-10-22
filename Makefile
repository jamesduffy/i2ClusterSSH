

.PHONY: clean build
build:
	pyinstaller --console --onefile --hidden-import configparser i2ClusterSSH.py


.PHONY: clean
clean:
	rm -r build/
	rm -r dist/


.PHONY: install
install:
	cp ./dist/i2ClusterSSH /usr/local/bin/i2cluster
