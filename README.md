# AI Job Recommender System with MCP

An AI-powered resume analysis and job discovery application built with **Streamlit**, **OpenRouter**, and **Apify**. Upload a PDF resume to receive an AI-generated resume summary, identify potential skill gaps, get a career-improvement roadmap, and discover relevant job listings from LinkedIn and Naukri.

The project also exposes LinkedIn and Naukri job-fetching functions as tools through an **MCP (Model Context Protocol) server**.

## Features

### Resume analysis
- Upload a resume in PDF format.
- Extract resume text using PyMuPDF.
- Generate a summary highlighting skills, education, and experience.
- Identify potential missing skills, certifications, and experience areas.
- Generate a suggested career roadmap.

### Job recommendations
- Generate job titles and search keywords from the resume summary.
- Fetch LinkedIn job listings through an Apify actor.
- Fetch Naukri job listings through an Apify actor.
- Display job title, company, location, and job link when those fields are returned by the respective actor.

### MCP server
The project includes an MCP server named **Job Recommender** with two tools:

| Tool | Description |
|---|---|
| `fetchlinkedin` | Fetch LinkedIn job listings using a search query. |
| `fetchnaukri` | Fetch Naukri job listings using a search query. |

The MCP server uses STDIO transport and can be launched by an MCP-compatible client.

## Tech Stack

- **Python**
- **Streamlit** – web application interface
- **OpenRouter** – LLM API access through the OpenAI-compatible Python SDK
- **OpenAI Python SDK** – sends chat completion requests to OpenRouter
- **PyMuPDF** – extracts text from PDF resumes
- **Apify Client** – runs the LinkedIn and Naukri scraping actors
- **python-dotenv** – loads API credentials from `.env`
- **MCP Python SDK (v1)** – exposes job-fetching functions as MCP tools

## Project Structure

```text
GenAI-Powered-Job-Recommender-System/
│
├── src/
│   ├── __init__.py
│   ├── helper.py          # PDF extraction and OpenRouter requests
│   └── job_api.py         # LinkedIn and Naukri Apify integrations
│
├── app.py                 # Streamlit application
├── mcp_server.py          # MCP server and job-fetching tools
├── requirements.txt       # Python dependencies
├── .env                   # Local API credentials (do not commit)
├── .gitignore
└── README.md
```

A local `venv/` directory is used for the Python environment and should not be committed.

## Prerequisites

- Python installed on your machine
- An OpenRouter API key
- An Apify account and API token
- Internet access

## Installation and Setup

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd GenAI-Powered-Job-Recommender-System
```

### 2. Create and activate a virtual environment

On Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

> The project currently pins the MCP dependency to version 1.x (`mcp[cli]<2`) because the server uses the `FastMCP` API from that version.

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
OPENROUTER_API_KEY=your_openrouter_api_key
APIFY_API_TOKEN=your_apify_api_token
```

Replace the placeholder values with your own credentials.

**Important:** Never commit `.env` or paste API keys into source code, screenshots, issues, or public repositories. The repository's `.gitignore` should include `.env`.

## Run the Streamlit Application

Make sure the virtual environment is activated, then run:

```bash
streamlit run app.py
```

Open the local URL printed in the terminal by Streamlit.

### Application workflow

1. Upload a PDF resume.
2. The application extracts its text.
3. OpenRouter generates the resume summary, skill-gap analysis, and career roadmap.
4. Select **Get Job Recommendations**.
5. The application generates job-search keywords and fetches listings from LinkedIn and Naukri through Apify.

## Run the MCP Server

The MCP server exposes the job-fetching functions as tools over STDIO.

With the virtual environment activated, run:

```bash
python mcp_server.py
```

The process may wait silently for an MCP client. This is expected for STDIO transport. Keep the process running while the client is connected.

### MCP tools

**`fetchlinkedin(search_query: str)`**

Fetches LinkedIn job listings for the supplied search query.

**`fetchnaukri(search_query: str)`**

Fetches Naukri job listings for the supplied search query.

To inspect and test the server locally, you can use MCP Inspector:

```bash
npx -y @modelcontextprotocol/inspector
```

In the Inspector, add a server using:
- **Transport:** `stdio (local process)`
- **Command:** the full path to `venv\Scripts\python.exe`
- **Arguments:** the full path to `mcp_server.py`

Use your project directory as the working directory if the Inspector provides that field. Connect and open the Tools tab to discover `fetchlinkedin` and `fetchnaukri`.

## Configuration Notes

- The OpenRouter client is configured in `src/helper.py` with the OpenAI-compatible base URL.
- The current model configured in the project is `openai/gpt-4o`. Availability and pricing depend on your OpenRouter account and the model provider.
- The LinkedIn and Naukri integrations run Apify actors configured in `src/job_api.py`.
- Apify actor runs can take longer than the MCP Inspector's default tool-call timeout. A timeout in Inspector does not necessarily mean the Apify actor itself has failed; check the Apify run status and logs.
- LinkedIn may rate-limit or reject scraping requests. Actor execution time and returned results can vary.

## Dependencies

The dependencies are listed in `requirements.txt`:

```text
streamlit
openai
pymupdf
python-dotenv
apify-client
mcp[cli]<2
```

## Security

- Keep API credentials in `.env`.
- Do not commit `.env` or expose its contents in screenshots or logs.
- If an API key is accidentally exposed, revoke or rotate it in the provider dashboard and update the local `.env` file.
- Do not share your Apify API token or OpenRouter API key.

## Future Improvements

- Add more robust error handling for API failures and actor timeouts.
- Make job-search location, result count, and filters configurable.
- Add job-result filtering and duplicate removal.
- Improve MCP tool execution for long-running Apify jobs.
- Add automated tests for resume parsing, API integrations, and MCP tools.


## 👩‍💻 Author

**Mousumi Badyakar**

---

⭐ If you find this project interesting, consider giving the repository a star!