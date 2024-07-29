import requests
from crewai import Agent, Task, Crew, Process
from langchain.llms import Ollama

try:
    response = requests.post('http://ollama:11434/api/generate',
                             json={"model": "openhermes",
                                   "prompt": "Test connection"})
    print("Connection successful:", response.json())

    # os.environ["OPENAI_API_KEY"] = "Your Key"
    #export OPENAI_API_KEY=sk-blablabla # on Linux/Mac
    ollama_model = Ollama(model="openhermes", base_url="http://ollama:11434")

    # Define seus agentes com funções e metas
    researcher = Agent(
        role='Researcher',
        goal='Discover new insights',
        backstory="""You're a world class
            researcher working on a major data science company""",
        verbose=True,
        allow_delegation=False,
        llm=ollama_model,
    )

    writer = Agent(
        role='Writer',
        goal='Create engaging content',
        backstory="""You're a famous technical writer,
            specialized on writing data related content""",
        verbose=True,
        allow_delegation=False,
        llm=ollama_model,
    )

    # Crie tarefas para seus agentes
    task1 = Task(description='Investigate the latest AI trends',
                 agent=researcher)
    task2 = Task(description='Write a blog post on AI advancements',
                 agent=writer)

    # Instancie sua equipe com um processo sequencial - DOIS AGENTES
    crew = Crew(
        agents=[researcher, writer],
        tasks=[task1, task2],
        llm=ollama_model,
        verbose=2,
        process=Process.sequential
    )

    # Coloque sua equipe para trabalhar
    result = crew.kickoff()

except Exception as e:
    print("Connection failed:", e)
