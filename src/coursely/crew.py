from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class Coursely():
    """Coursely Online Course Builder crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def curriculum_designer(self) -> Agent:
        return Agent(
            config=self.agents_config['curriculum_designer'], # type: ignore[index]
            verbose=True
        )

    @agent
    def lesson_planner(self) -> Agent:
        return Agent(
            config=self.agents_config['lesson_planner'], # type: ignore[index]
            verbose=True
        )

    @agent
    def quiz_generator(self) -> Agent:
        return Agent(
            config=self.agents_config['quiz_generator'], # type: ignore[index]
            verbose=True
        )

    @task
    def curriculum_task(self) -> Task:
        return Task(
            config=self.tasks_config['curriculum_task'], # type: ignore[index]
        )

    @task
    def lesson_task(self) -> Task:
        return Task(
            config=self.tasks_config['lesson_task'], # type: ignore[index]
        )

    @task
    def quiz_task(self) -> Task:
        return Task(
            config=self.tasks_config['quiz_task'], # type: ignore[index]
            output_file='course_output.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Coursely Online Course Builder crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
