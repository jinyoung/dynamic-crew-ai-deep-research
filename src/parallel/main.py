#!/usr/bin/env python
import asyncio
import warnings
from datetime import datetime

from parallel.flows.dynamic_report_flow import DynamicReportFlow

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


async def run_dynamic_report_generation(topic):
    """
    Runs the dynamic report generation flow.
    
    Args:
        topic (str): The topic for the report
        
    Returns:
        str: The final generated report
    """
    print("-" * 50)
    print(f"Dynamic Report Generation for topic: {topic}")

    # Initialize the flow with the topic in the initial state
    flow = DynamicReportFlow()
    flow.state.topic = topic
    
    # Kick off the flow
    result = await flow.kickoff_async()
    
    print("\nFinal Report Generated:\n")
    print("-" * 50)
    
    return result


def run():
    """
    Orchestrates the dynamic report generation process.
    """
    current_year = str(datetime.now().year)
    print("\n=== Dynamic Report Generation System ===\n")
    print(f"Current Year: {current_year}")

    # Example topic - this could be taken from command line arguments
    topic = "Artificial Intelligence in Healthcare"
    
    # Run the dynamic report generation flow
    final_report = asyncio.run(run_dynamic_report_generation(topic))
    
    print(f"Report on '{topic}' has been successfully generated.")
    print("Final Report Length:", len(final_report))
    
    # Save the report to a file
    filename = f"report_{topic.replace(' ', '_').lower()}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(filename, "w") as f:
        f.write(final_report)
    
    print(f"Report saved to {filename}")


if __name__ == "__main__":
    run() 