from crewai.tools import tool
from ddgs import DDGS


@tool("Search CRM market intelligence")
def search_crm_market(query: str) -> str:
    """Search the web for CRM product updates, pricing,
    partnerships and market developments using a specific query."""

    try:
        results = DDGS().text(query, max_results=3)

        if not results:
            return "No relevant search results found."

        formatted = []

        for item in results:
            formatted.append(
                f"Title: {item.get('title', 'N/A')}\n"
                f"URL: {item.get('href', 'N/A')}\n"
                f"Snippet: {item.get('body', 'N/A')}"
            )

        return "\n\n".join(formatted)

    except Exception as e:
        return f"Search failed: {str(e)}"
