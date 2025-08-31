import os 

try:
    from dotenv import load_dotenv
    load_dotenv()
    
    MODEL_NAME = os.environ.get("GOOGLE_GENAI_MODEL", "gemini-2.0-flash")
except ImportError:
    print("Warning: python-dotenv not installed. Ensure API key is set")
    MODEL_NAME = "gemini-2.0-flash"

from google.adk.agents import LlmAgent, SequentialAgent
from google.adk.tools import google_search

from marketing_campaign_agent.instructions import(
    MARKET_RESEARCH_INSTRUCTION
)

market_research_agent = LlmAgent(
    name = "Market Researcher",
    model = MODEL_NAME,
    instructions = MARKET_RESEARCH_INSTRUCTION,
    tools = [google_search]
    outouput_key = "market_research_summary"
)