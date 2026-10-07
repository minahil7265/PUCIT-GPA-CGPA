# PUCIT GPA/CGPA Advisor

A conversational AI agent that calculates semester GPA, projects CGPA, 
and tells you what grades you need to hit targets.

### Prerequisites
- Python 3.8+
- Groq API key 

## Setup
1. `pip install -r requirements.txt`
2. `cp .env.example .env` add groq key in .env
3. Terminal: `python agent.py` | Web: `streamlit run app.py`

## Files

- `llm.py` - Groq setup
- `tools.py` - All calculations
- `agent.py` - Agent logic + system prompt
- `app.py` - Streamlit UI 