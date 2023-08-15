
.PHONY: restart
restart:
	sudo systemctl restart myflaskapp.service
.PHONY: status
status:
	sudo systemctl status myflaskapp.service


.PHONY: install
# if environment is pi, ignore
# otherwise, do pip install -r requirements.txt with a new virtualenv
install:
ifeq ($(ENVIRONMENT),pi)
	@echo "Environment is pi, skipping pip install"
else
	@echo "Environment is not pi, installing requirements.txt"
	@echo "Creating virtualenv"
	@virtualenv -p python3 venv
	@echo "Installing requirements.txt"
	@venv/bin/pip install -r requirements.txt
endif


.PHONY: run
run:
	@echo "Running app"
	@venv/bin/flask run --host=0.0.0.0 --port=5000