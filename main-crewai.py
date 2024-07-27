from crewai import Agent, Task, Crew, Process

from langchain.llms import Ollama
ollama_model = Ollama(model="openhermes")

# Define your agents with roles and goals
researcher = Agent(
  role='Researcher',
  goal='Discover new insights',
  backstory="""You're a world class researcher
    working on a major data science company""",
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
  llm=ollama_model
)

# Create tasks for your agents
task1 = Task(description='Investigate the latest AI trends', agent=researcher)
task2 = Task(description='Write a blog post on AI advancements', agent=writer)

# Instantiate your crew with a sequential process - TWO AGENTS!
crew = Crew(
  agents=[researcher, writer],
  tasks=[task1, task2],
  llm=ollama_model,
  verbose=2,
  process=Process.sequential
)

# Get your crew to work!
result = crew.kickoff()
