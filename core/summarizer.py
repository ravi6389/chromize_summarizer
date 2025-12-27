from firecrawl import Firecrawl
from langchain_openai import AzureChatOpenAI
import os
from langchain_groq import ChatGroq



firecrawl = Firecrawl(api_key=os.getenv("FIRECRAWL_API_KEY"))
GROQ_API_KEY = os.getenv('GROQ_API_KEY')
llm = ChatGroq(temperature=0.8, groq_api_key=GROQ_API_KEY,
            model_name="llama-3.3-70b-versatile", streaming=True)


def summarize_url(url: str) -> str:
    result = firecrawl.scrape(url=url, formats=["markdown"])

    if hasattr(result, "markdown"):
        content = result.markdown
    elif isinstance(result, dict):
        content = result.get("data", {}).get("markdown", "")
    else:
        content = ""

    content = content[:8000]

    prompt = f"""
    Summarize the following webpage in clear bullet points:

    {content}
    """

    return llm.invoke(prompt).content
