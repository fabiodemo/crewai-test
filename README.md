# crewai-test

## Build the dockerfile

`docker build -t crewai .`

## Setup the container for ollama

`docker compose -f docker-compose-ollama.yml up -d`

## Setup the container for python

`docker compose up -d`

## Install model openhermes

`docker exec -it ollama ollama pull openhermes`

## Verify if model is download succesfully

`docker exec -it ollama ls /root/.ollama/models`

## Run the main-crew script

`docker exec -it aigen_crewai python3 main-crewai.py`


### Credits:
Code based on:
    - [Deploy local LLMs like containers - OLLama Docker](https://fossengineer.com/selfhosting-llms-ollama/)
    - [Local AI Agents with CrewAI (and Ollama)](https://fossengineer.com/ai-agents-crewai/)