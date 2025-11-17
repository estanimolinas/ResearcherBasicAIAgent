from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain.agents.structured_output import ToolStrategy
from tools import search_tool, wiki_tool, save_to_txt

load_dotenv()


class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]


model = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0,
)

tools = [search_tool, wiki_tool, save_to_txt]

agent = create_agent(
    model=model,
    tools=tools,
    response_format=ToolStrategy(ResearchResponse),
)

user_query = input("¿Qué querés investigar? ")

result = agent.invoke(
    {
        "messages": [
            {"role": "user", "content": user_query}
        ]
    }
)

# LangChain 1.0 + ToolStrategy devuelve el objeto en result["structured_response"]
try:
    structured = result["structured_response"]
    print(structured)
except Exception as e:
    print("Error leyendo structured_response:", e)
    print("Result completo:", result)
