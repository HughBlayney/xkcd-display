
.PHONY: restart
restart:
	sudo systemctl restart myflaskapp.service
.PHONY: status
status:
	sudo systemctl status myflaskapp.service


