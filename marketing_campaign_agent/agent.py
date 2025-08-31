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
    MARKET_RESEARCH_INSTRUCTION,
    CAMPAIGN_ORCHESTRATOR_INSTRUCTION,
    MESSAGING_STRATEGIST_INSTRUCTION,
    AD_COPY_WRITER_INSTRUCTION,
    VISUAL_SUGGESTER_INSTRUCTION,
    FORMATTER_INSTRUCTION
)

market_research_agent = LlmAgent(
    name = "MarketResearcher",
    model = MODEL_NAME,
    description = MARKET_RESEARCH_INSTRUCTION,
    tools = [google_search],
    output_key = "market_research_summary"
)

messaging_strategist_agent = LlmAgent(
    name="MessagingStrategist",
    model = MODEL_NAME,
    instruction=MESSAGING_STRATEGIST_INSTRUCTION,
    output_key="key_messaging"
)


campaign_orchestrator = SequentialAgent(
    name = "MarketingCampaignAssistant",
    description = CAMPAIGN_ORCHESTRATOR_INSTRUCTION,
    sub_agents = [
        market_research_agent
    ]
)


root_agent = campaign_orchestrator