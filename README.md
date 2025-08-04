# Research Agent Playground

This project provides an AI-powered research agent using Phi, OpenAI GPT-4o, and web search tools (DuckDuckGo, Exa).  
You can interact with the agent through a Playground UI or script to generate research-grade articles on any topic.

---

## Files

- `playground.py` — Launches an interactive Playground app (web UI) for the research agent.
- `Research_agent.py` — Script example to use the research agent for research tasks from the command line.

---

## Features

- **Automated research:** Searches the web for top 5 relevant links on a topic.
- **Content extraction:** Reads and summarizes articles from URLs.
- **Article generation:** Produces well-structured, NYT-style research articles.
- **Interactive UI:** Start the Playground app and chat with your custom research agent.

---

## Requirements

- Python 3.8+
- [phidata](https://phidata.com/) and required libraries:
    ```
    pip install phi
    ```
- OpenAI API Key  
- Exa API Key (for advanced web search)

---

## Setup & Running

### 1. Install Dependencies

2. Set API Keys
Replace "YOUR KEY" with your actual API keys in both files:

OPENAI_API_KEY (required)

PHI_API_KEY (optional, for some tools)

EXA_API_KEY (for ExaTools)

set these as environment variables in your shell:

export OPENAI_API_KEY=sk-xxxxxx
export EXA_API_KEY=ex-xxxxxx

3. Run the Playground UI

python playground.py
Opens a local web app for chatting with your Research Agent.

4. Run Example Research Agent Script

python Research_agent.py
Runs a sample research query and prints the output in the terminal.

How It Works
playground.py creates an agent using GPT-4o and search tools, then launches a web app for interactive research.

Research_agent.py can be modified to automate or script research tasks (examples included in the file).

Sample Use Cases
Summarize latest trends in AI, technology, or science.

Prepare background articles for journalism, blogs, or business reports.

Quickly extract and synthesize knowledge from top web sources.
