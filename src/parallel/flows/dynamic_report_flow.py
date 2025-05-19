import asyncio
from typing import Dict, List, Any

from crewai.crew import Crew
from crewai.flow.flow import Flow, and_, listen, router, start
from pydantic import BaseModel, Field

from ..crews.planning_crew.PlanningCrew import PlanningCrew
from ..crews.report_crew.ReportCrew import ReportCrew


class DynamicReportState(BaseModel):
    """State for the dynamic report generation flow."""
    topic: str = ""
    toc: List[Dict[str, Any]] = Field(default_factory=list)
    agent_configs: List[Dict[str, Any]] = Field(default_factory=list)
    task_configs: List[Dict[str, Any]] = Field(default_factory=list)
    section_reports: Dict[str, str] = Field(default_factory=dict)
    final_report: str = ""


class DynamicReportFlow(Flow[DynamicReportState]):
    """
    A flow that dynamically plans and generates a report on a given topic.
    
    This flow consists of two main phases:
    1. Planning: Generates a table of contents and configures agents and tasks
    2. Execution: Dynamically creates and executes agents and tasks to write each section
    """

    def __init__(self):
        super().__init__(
            description="Flow for dynamic report generation based on a given topic",
            state_type=DynamicReportState
        )

    @start()
    async def initialize_flow(self):
        """Initialize the flow with the input topic."""
        # In newer CrewAI versions, the inputs are stored in self.state
        if hasattr(self, 'inputs') and "topic" in self.inputs:
            self.state.topic = self.inputs["topic"]
            print(f"Initialized flow with topic: {self.state.topic}")
            return self.state.topic
        elif hasattr(self, 'state') and hasattr(self.state, 'topic') and self.state.topic:
            print(f"Using topic from state: {self.state.topic}")
            return self.state.topic
        else:
            # Fallback to a default topic for testing
            default_topic = "Artificial Intelligence in Healthcare"
            print(f"No topic provided, using default: {default_topic}")
            self.state.topic = default_topic
            return default_topic

    @listen("initialize_flow")
    async def plan_report(self):
        """Plan the report structure and generate TOC."""
        print(f"Planning report for topic: {self.state.topic}")
        
        planning_crew = PlanningCrew().crew()
        
        planning_result = await planning_crew.kickoff_async(inputs={
            "topic": self.state.topic
        })
        
        # Extract TOC and agent/task configs from planning result
        try:
            result_data = planning_result.raw
            
            # In a real implementation, you might want to parse this as JSON
            # For simplicity, we're assuming a structured output that can be parsed
            # The actual implementation would need proper parsing based on the output format
            
            # This is a placeholder for demonstration
            parsed_data = result_data
            
            self.state.toc = parsed_data.get("toc", [])
            self.state.agent_configs = parsed_data.get("agent_configs", [])
            self.state.task_configs = parsed_data.get("task_configs", [])
            
            print(f"Report planned with {len(self.state.toc)} sections")
            return self.state.toc
        except Exception as e:
            print(f"Error parsing planning result: {e}")
            # Fallback to a simple TOC for demonstration
            self.state.toc = [
                {"title": "Introduction", "id": "intro"},
                {"title": f"Current State of {self.state.topic}", "id": "current_state"},
                {"title": "Key Technologies", "id": "technologies"},
                {"title": "Applications", "id": "applications"},
                {"title": "Future Directions", "id": "future"},
                {"title": "Conclusion", "id": "conclusion"}
            ]
            return self.state.toc

    @listen("plan_report")
    async def generate_report_sections(self):
        """Generate each section of the report in parallel."""
        print("Generating report sections in parallel...")
        
        # Create tasks to generate each section
        section_tasks = []
        for section in self.state.toc:
            section_id = section["id"]
            section_title = section["title"]
            
            section_task = self.create_section_task(section_id, section_title)
            section_tasks.append(section_task)
        
        # Execute all section tasks in parallel
        section_results = await asyncio.gather(*section_tasks)
        
        # Store the results in the state
        for i, section in enumerate(self.state.toc):
            self.state.section_reports[section["id"]] = section_results[i]
        
        print(f"Generated {len(section_results)} report sections")
        return self.state.section_reports

    async def create_section_task(self, section_id, section_title):
        """Create a task to generate a specific section."""
        print(f"Creating task for section: {section_title}")
        
        # Initialize the report crew dynamically
        report_crew = ReportCrew().section_crew(
            section_id=section_id, 
            section_title=section_title,
            topic=self.state.topic
        )
        
        # Execute the crew to generate the section
        report_result = await report_crew.kickoff_async(inputs={
            "topic": self.state.topic,
            "section_id": section_id,
            "section_title": section_title
        })
        
        return report_result.raw if report_result else ""

    @listen("generate_report_sections")
    def compile_final_report(self):
        """Compile all sections into the final report."""
        print("Compiling final report...")
        
        # Create the report header
        report = f"# REPORT: {self.state.topic}\n\n"
        report += f"## Table of Contents\n\n"
        
        # Add the table of contents
        for i, section in enumerate(self.state.toc):
            report += f"{i+1}. {section['title']}\n"
        
        report += "\n\n"
        
        # Add each section content
        for section in self.state.toc:
            section_id = section["id"]
            section_title = section["title"]
            section_content = self.state.section_reports.get(section_id, "No content generated for this section.")
            
            report += f"## {section_title}\n\n"
            report += f"{section_content}\n\n"
        
        # Store the final report in the state
        self.state.final_report = report
        
        print("Final report compiled successfully")
        return self.state.final_report


def plot():
    flow = DynamicReportFlow()
    flow.plot() 