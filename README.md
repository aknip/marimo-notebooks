# Start

Terminal:
docker compose up

Browser: 
http://localhost:1865/admin/


# Config for Ollama LLM
- Base URL:
    http://host.docker.internal:11434
- Model: For example:
    mixtral-8x7b-instruct-v0.1-q4_0-32k
    gemma-7b-instruct-8k
- all other params can be left empty, will be filled automatically after saving


# Information

## How to install with Docker Compose
https://cheshire-cat-ai.github.io/docs/quickstart/installation-configuration/

Um von Chehsire auf lokales Ollama zugreifen zu können, muss in  Docker der Netzwerkzugriff auf den Host freigeschaltet werden:
	- Docker:  `--add-host=host.docker.internal:host-gateway`
	- In Docker Compose muss ergänzt werden:
		extra_hosts:
			- "host.docker.internal:host-gateway"
	- Danach kann Cheshire aus Docker heraus auf den Host zugreifen. Die URL ist dann nicht "localhost" oder "127.0.0.1" sondern `http://host.docker.internal`