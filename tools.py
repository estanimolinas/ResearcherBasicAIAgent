from datetime import datetime

from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_core.tools import tool

# Wrapper de Wikipedia
api_wrapper = WikipediaAPIWrapper(
    top_k_results=1,
    doc_content_chars_max=1000,
)
wiki_tool = WikipediaQueryRun(api_wrapper=api_wrapper)

# Búsqueda web (DuckDuckGo)
search_tool = DuckDuckGoSearchRun()

# Guardar a TXT como herramienta
@tool
def save_to_txt(data: str) -> str:
    """Save structured research data to a local text file with a timestamp."""
    filename = "research_output.txt"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_text = (
        f"--- Research Output ---\n"
        f"Timestamp: {timestamp}\n\n"
        f"{data}\n\n"
    )

    with open(filename, "a", encoding="utf-8") as f:
        f.write(formatted_text)

    return f"Data successfully saved to {filename}"
