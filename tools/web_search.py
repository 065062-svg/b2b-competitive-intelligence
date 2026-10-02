from crewai.tools import BaseTool
from ddgs import DDGS
from pydantic import BaseModel, Field


class WebSearchInput(BaseModel):
    query: str = Field(description="Search query for competitive intelligence")


class WebSearchTool(BaseTool):
    name: str = "Web Search"
    description: str = (
        "Search the web for competitor information, product launches, "
        "pricing updates, and market trends. Keep results relevant "
        "to the company named in the query."
    )
    args_schema: type[BaseModel] = WebSearchInput

    def _run(self, query: str) -> str:
        try:
            results = DDGS().text(query, max_results=3)

            if not results:
                return "No search results found."

            companies = {
                "salesforce": ["salesforce"],
                "hubspot": ["hubspot"],
                "freshworks": ["freshworks", "freshsales", "freshdesk"]
            }

            query_lower = query.lower()
            target = next(
                (name for name in companies if name in query_lower),
                None
            )

            formatted_results = []

            for item in results:
                title = item.get("title", "No title")
                url = item.get("href", "No URL")
                summary = item.get("body", "No summary")

                if target:
                    title_lower = title.lower()

                    relevant_title = any(
                        keyword in title_lower
                        for keyword in companies[target]
                    )

                    if not relevant_title:
                        continue

                summary = summary[:400]

                formatted_results.append(
                    f"Search query: {query}\n"
                    f"Title: {title}\n"
                    f"URL: {url}\n"
                    f"Summary: {summary}"
                )

            if not formatted_results:
                return (
                    f"No relevant results passed the company filter "
                    f"for query: {query}"
                )

            return "\n\n".join(formatted_results)

        except Exception as e:
            return f"Search error: {e}"