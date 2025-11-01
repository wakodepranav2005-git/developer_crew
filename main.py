# main.py

from crewai import Crew, Process
from src.agents import planner, researcher, developer # <-- Import 'developer', not 'writer'
from src.tasks import get_tasks

# --- 6. Create the Crew ---
project_crew = Crew(
    agents=[planner, researcher, developer], # <-- Add 'developer' to the list
    tasks=get_tasks(),
    process=Process.sequential,
    verbose=True
)

# --- 7. Run the Crew in a Loop ---
if __name__ == "__main__":
    print("🚀 Starting the Developer Crew...")
    print("---------------------------------")
    print("Enter your request, or type 'exit' to quit.")

    while True:
        # Get input from the user
        user_request = input("\n> ")

        if user_request.lower() == 'exit':
            print("👋 Goodbye!")
            break
        
        if not user_request:
            continue

        # Create the inputs dictionary for this run
        inputs = {'user_request': user_request}

        # Kick off the crew with the dynamic inputs
        result = project_crew.kickoff(inputs=inputs)

        print("\n✅ Crew run completed!")
        print("Final Result:")
        print(result)
        print("---------------------------------")
        print("Enter your next request...")