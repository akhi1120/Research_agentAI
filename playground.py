from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.exa import ExaTools
from phi.playground import Playground, serve_playground_app

import os
# Set OpenAI API Key
os.environ["OPENAI_API_KEY"] ="YOUR KEY"
os.environ["EXA_API_KEY"] = "YOUR KEY"

# Define the Research Agent with multiple tools
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

# Create Playground app
try:
    playground = Playground(agents=[research_agent])  # Create Playground instance
    app = playground.get_app()  # Get the FastAPI app instance

    # Ensure the script runs only when executed directly
    if __name__ == "__main__":
        serve_playground_app(app)  # Start the Phidata Playground UI
except Exception as e:
    print(f"Error starting Playground: {e}")
