.PHONY: shell
shell:
	docker-compose build && \
	docker-compose run --rm cop-markov-twitter bash
