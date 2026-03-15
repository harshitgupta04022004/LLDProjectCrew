from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai.memory import LongTermMemory, ShortTermMemory, EntityMemory
from crewai.memory.storage.rag_storage import RAGStorage
from crewai.memory.storage.ltm_sqlite_storage import LTMSQLiteStorage


def make_llm(model: str) -> LLM:
    """Create an Ollama-backed LLM instance."""
    return LLM(
        model=f"ollama/{model}",
        base_url="http://localhost:11434",
        temperature=0.2
    )


@CrewBase
class LLDProjectCrew():
    """LLD Project crew for validating UML Class Diagrams"""

    agents_config = 'config/agents.yaml'
    tasks_config  = 'config/tasks.yaml'

    # ─── Agents ───────────────────────────────────────────────────────────────

    @agent
    def structural_validator(self) -> Agent:
        return Agent(
            config=self.agents_config['structural_validator'],
            llm=make_llm("qwen3-coder:480b-cloud"),
            verbose=True,
            memory=True
        )

    @agent
    def relationship_validator(self) -> Agent:
        return Agent(
            config=self.agents_config['relationship_validator'],
            llm=make_llm("qwen3-coder:480b-cloud"),
            verbose=True,
            memory=True
        )

    @agent
    def design_quality_analyzer(self) -> Agent:
        return Agent(
            config=self.agents_config['design_quality_analyzer'],
            llm=make_llm("qwen3-coder:480b-cloud"),
            verbose=True,
            memory=True
        )

    @agent
    def feedback_evaluator(self) -> Agent:
        return Agent(
            config=self.agents_config['feedback_evaluator'],
            llm=make_llm("qwen3-coder:480b-cloud"),
            verbose=True,
            memory=True
        )

    # ─── Tasks ────────────────────────────────────────────────────────────────

    @task
    def structural_validation_task(self) -> Task:
        return Task(config=self.tasks_config['structural_validation_task'])

    @task
    def relationship_validation_task(self) -> Task:
        return Task(config=self.tasks_config['relationship_validation_task'])

    @task
    def design_quality_analysis_task(self) -> Task:
        return Task(config=self.tasks_config['design_quality_analysis_task'])

    @task
    def feedback_evaluation_task(self) -> Task:
        return Task(config=self.tasks_config['feedback_evaluation_task'])

    # ─── Crew ─────────────────────────────────────────────────────────────────

    @crew
    def crew(self) -> Crew:
        """Creates the LLD validation crew"""

        manager = Agent(
            config=self.agents_config['orchestrator'],
            llm=make_llm("qwen3-coder:480b-cloud"),
            verbose=True,
            memory=True,
            allow_delegation=True
        )

        return Crew(
            manager_agent=manager,          # ✅ was: orchestrator= (wrong)
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
            long_term_memory=LongTermMemory(
                storage=LTMSQLiteStorage(
                    db_path='./memory/long_term_memory_storage.db'
                )
            ),
            short_term_memory=ShortTermMemory(
                storage=RAGStorage(
                    embedder_config={
                        "provider": "ollama",
                        "config": {"model": "qwen3-embedding:0.6b"}
                    },
                    type="short_term",
                    path='./memory/'
                )
            ),
            entity_memory=EntityMemory(
                storage=RAGStorage(
                    type="entity",
                    embedder_config={
                        "provider": "ollama",
                        "config": {"model": "qwen3-embedding:0.6b"}
                    },
                    path='./memory'
                )
            ),
        )