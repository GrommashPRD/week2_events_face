start:
	@docker build -t events-face .
	@docker-compose up -d

stop:
	@docker-compose down


.PHONY: start stop