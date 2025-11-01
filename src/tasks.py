# src/tasks.py

from crewai import Task
from src.agents import planner, researcher, developer  # <-- Import 'developer', not 'writer'

def get_tasks():
    # --- 5. Define Tasks (3 Tasks) ---
    
    # task_plan (unchanged)
    task_plan = Task(
        description="Create a plan to fulfill this request: '{user_request}'. "
                    "Your final output must be a simple plan detailing the search query and the filename.",
        expected_output="A plan including the string for the search query and the string for the filename.",
        agent=planner,
        human_input=True
    )

    # task_research (unchanged)
    task_research = Task(
        description="Execute the web search using the query from the planner's report.",
        expected_output="A detailed summary of the research findings.",
        agent=researcher,
        context=[task_plan]
    )

    # *** THIS IS THE CHANGED TASK ***
    task_write = Task(
        description="Take the research findings and the filename from the plan. "
                    "Write the complete, raw source code for the file. "
                    "Ensure the code is functional and contains NO markdown formatting or extra text. "
                    "Save this raw code to the specified filename using the file writing tool.",
        expected_output="The final file path of the saved code file (e.g., 'output/filename.c').",
        agent=developer,  # <-- Assign to the new 'developer' agent
        context=[task_research, task_plan]
    )
    
    return [task_plan, task_research, task_write]