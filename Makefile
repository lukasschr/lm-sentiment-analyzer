VERSION=1.0.1
DOCKER_IMAGE_NAME=lm-sentiment-analyzer:$(VERSION)
DOCKER_CONTAINER_NAME=lm-sentiment-analyzer

build:
	docker build -t $(DOCKER_IMAGE_NAME) .

run:
	-docker rm -f $(DOCKER_CONTAINER_NAME) 2>/dev/null || true
	docker run -d -p 8000:8000 --name $(DOCKER_CONTAINER_NAME) $(DOCKER_IMAGE_NAME)

stop:
	docker stop $(DOCKER_CONTAINER_NAME) || true

delete:
	docker rm $(DOCKER_CONTAINER_NAME) || true
	docker rmi $(DOCKER_IMAGE_NAME) || true