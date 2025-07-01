from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.exa import ExaTools
import os

# Set OpenAI API Key
os.environ["OPENAI_API_KEY"] ="YOUR KEY"
os.environ["PHI_API_KEY"] = "YOUR KEY"
os.environ["EXA_API_KEY"] = "YOUR KEY"

research_agent = Agent(
    name="Research Agent",
    model=OpenAIChat(id="gpt-4o"),
    tools=[DuckDuckGo(), ExaTools()],
    description="You are a senior NYT researcher writing an article on a topic.",
    instructions=[
        "For a given topic, search for the top 5 links.",
        "Then read each URL and extract the article text, if a URL isn't available, ignore it.",
        "Analyse and prepare an NYT worthy article based on the information.",
    ],
    markdown=True,
    show_tool_calls=True,
    add_datetime_to_instructions=True,
)


# Example Calls
research_agent.print_response("Summarize the latest advancements in AI and deep learning.")  # AI research
# research_agent.print_response("Analyze recent advancements in quantum computing.")  # Research on Quantum Computing
