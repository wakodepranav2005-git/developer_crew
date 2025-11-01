# src/agents.py

from crewai import Agent, LLM
from src.custom_tools import DuckDuckGoSearchTool, SafeFileWriteTool

# --- 3. Setup Tools & LLM ---
search_tool = DuckDuckGoSearchTool()
write_tool = SafeFileWriteTool()

local_llm = LLM(
    model="ollama/yxchia/qwen2.5-3b-instruct:Q4_K_M",
    base_url="http://localhost:11434"
)

# --- 4. Create Agents (3 Agents) ---

# Planner (unchanged)
planner = Agent(
    role="Project Planner",
    goal="Analyze a user's request and create a clear, step-by-step plan. "
         "The plan must include the exact search query to use and the exact filename for the final output.",
    backstory="You are a meticulous planner. You break down complex goals into simple, actionable steps. "
              "You are precise and your output is always clear.",
    llm=local_llm,
    verbose=True
)

# Researcher (unchanged)
researcher = Agent(
    role="Web Research Specialist",
    goal="Use the provided search query to find the most relevant and up-to-date information from the web.",
    backstory="You are an expert web researcher, skilled at sifting through noise to find high-quality, "
              "factual information. You use the DuckDuckGo search tool effectively.",
    tools=[search_tool],
    llm=local_llm,
    verbose=True
)

# *** THIS IS THE CHANGED AGENT ***
# Agent 3: The Developer (replaces Writer)
developer = Agent(
    role="Software Developer",
    goal="Take the research findings and the target filename. Write clean, functional, and correct "
         "source code to fulfill the request. You must output *only* the raw source code, with no "
         "markdown formatting (like ```) or explanatory text.",
    backstory="You are an expert developer. You write code, not documentation. "
              "You follow the plan and use the research to write perfect, raw source code. "
              "You only use the tools you are given to write the file.",
    tools=[write_tool],
    llm=local_llm,
    verbose=True
)