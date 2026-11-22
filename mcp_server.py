from mcp.server.fastmcp import FastMCP
from src.job_api import fetch_linkedin_jobs, fetch_naukri_jobs

mcp = FastMCP("Job Recommender")


@mcp.tool()
def fetchlinkedin(search_query: str) -> list:
    """
    Fetch LinkedIn job listings using a job title or search keyword.

    Args:
        search_query: Job title or keywords, for example "Python Developer".
    """
    return fetch_linkedin_jobs(search_query)


@mcp.tool()
def fetchnaukri(search_query: str) -> list:
    """
    Fetch Naukri job listings using a job title or search keyword.

    Args:
        search_query: Job title or keywords, for example "Data Scientist".
    """
    return fetch_naukri_jobs(search_query)


if __name__ == "__main__":
    mcp.run(transport="stdio")
