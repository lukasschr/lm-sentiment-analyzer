VERSION=dev
DOCKER_IMAGE_NAME=lm-sentiment-analyzer:$(VERSION)
DOCKER_CONTAINER_NAME=lm-sentiment-analyzer

build:
	docker build -t $(DOCKER_IMAGE_NAME) .

run:
	docker run -d -p 8000:8000 --name $(DOCKER_CONTAINER_NAME) $(DOCKER_IMAGE_NAME)

stop:
	docker stop $(DOCKER_CONTAINER_NAME) || true

delete:
	docker rmi $(IMAGE_NAME) || true