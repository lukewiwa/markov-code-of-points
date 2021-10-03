.PHONY: shell
shell:
	docker-compose build && \
	docker-compose run --rm cop-markov-twitter bash

.PHONY: deploy
deploy:
	npm --prefix=markov-code-of-points-cdk run synth && \
	npm --prefix=markov-code-of-points-cdk run deploy
