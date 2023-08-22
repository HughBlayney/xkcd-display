include .env

.PHONY: restart
restart:
	sudo systemctl restart myflaskapp.service
.PHONY: status
status:
	sudo systemctl status myflaskapp.service

export

.PHONY: install
# if environment is pi, ignore
# otherwise, do pip install -r requirements.txt with a new virtualenv
install:
ifeq ($(XKCD_ENVIRONMENT),pi)
	@echo "Environment is pi, skipping pip install"
else
	@echo "Environment is not pi, installing requirements.txt"
	@echo "Creating virtualenv"
	@virtualenv -p python3 venv
	@echo "Installing requirements.txt"
	@venv/bin/pip install -r requirements.txt
endif

.PHONY: debug
debug:
	@echo "Running app in debug mode"
	@venv/bin/flask run

.PHONY: run
start:
	@echo "Running app"
	@venv/bin/gunicorn -w 1 -b 0.0.0.0:5000 app:app --access-logfile -

.PHONY: screen
screen:
	@echo "Running screen server"
	@echo "Opening browser to https://$$XKCD_SCREEN_SOCKET_URL"
	@node screen_server.js & \
	server_pid=$$!; \
	open https://$$XKCD_SCREEN_SOCKET_URL; \
	wait $$server_pid