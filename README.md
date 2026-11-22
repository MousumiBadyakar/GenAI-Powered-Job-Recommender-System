# 🤖 AI Job Recommender

**Turn your resume into actionable career insights and job opportunities.**

AI Job Recommender is a Streamlit application that analyzes a PDF resume, highlights potential skill gaps, suggests a career roadmap, and finds relevant job listings from LinkedIn and Naukri. It uses OpenRouter for AI-powered analysis and Apify actors to retrieve job listings.

The project also includes an **MCP (Model Context Protocol) server** that exposes LinkedIn and Naukri job-fetching functions as tools for MCP-compatible clients.

<p align="center">
  <a href="https://genai-powered-job-recommender-system-cu2jcrkfqp8izeyrz8f6yb.streamlit.app/">
    <img src="https://img.shields.io/badge/🚀_Try_Live_Demo-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Live Demo">
  </a>
</p>

---

## 🌐 Live Demo

Try the deployed application here:

👉 **[AI Job Recommender – Live on Streamlit](https://genai-powered-job-recommender-system-cu2jcrkfqp8izeyrz8f6yb.streamlit.app/)**

---

## ✨ Features

### 📄 AI-Powered Resume Analysis
- Upload your resume in PDF format.
- Extract resume text using **PyMuPDF**.
- Generate an AI summary of your skills, education, and experience.
- Identify potential skill gaps, missing certifications, and experience areas.
- Receive a suggested career roadmap with skills to learn and areas to improve.

### 💼 Job Recommendations
- Generate relevant job titles and search keywords from your resume summary.
- Fetch job listings from **LinkedIn** using Apify.
- Fetch job listings from **Naukri** using Apify.
- View job titles, company names, locations, and application links when returned by the source.

### 🤖 MCP Server Integration
The project includes an MCP server named **Job Recommender**, exposing two tools:

| MCP Tool | Description |
|---|---|
| `fetchlinkedin` | Fetch LinkedIn job listings using a search query. |
| `fetchnaukri` | Fetch Naukri job listings using a search query. |

The server uses **STDIO transport** and can be connected to MCP-compatible clients.

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| 🐍 Python | Core programming language |
| 🎈 Streamlit | Interactive web application |
| 🧠 OpenRouter | LLM API access for resume analysis |
| 🔗 OpenAI Python SDK | OpenAI-compatible requests to OpenRouter |
| 📑 PyMuPDF | PDF text extraction |
| 🕷️ Apify | LinkedIn and Naukri job scraping actors |
| 🔌 MCP Python SDK | Exposes job-fetching functions as MCP tools |
| 🔐 python-dotenv | Loads API credentials from environment variables |

---

## 📂 Project Structure

```text
GenAI-Powered-Job-Recommender-System/
│
├── src/
│   ├── __init__.py
│   ├── helper.py          # PDF extraction and OpenRouter integration
│   └── job_api.py         # LinkedIn and Naukri Apify integrations
│
├── app.py                 # Streamlit application
├── mcp_server.py          # MCP server and job-fetching tools
├── requirements.txt       # Python dependencies
├── .env                   # Local API credentials (never commit)
├── .gitignore
└── README.md
```

> The local `venv/` virtual environment is not included in the repository.

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone <your-repository-url>
cd GenAI-Powered-Job-Recommender-System
```

### 2️⃣ Create and activate a virtual environment

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux**

```bash
python -m venv venv
source venv/bin/activate
```

### 3️⃣ Install dependencies

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

> ℹ️ The project currently uses `mcp[cli]<2` because the MCP server is implemented with the `FastMCP` API from MCP SDK v1.

### 4️⃣ Configure environment variables

Create a `.env` file in the project root:

```env
OPENROUTER_API_KEY=your_openrouter_api_key
APIFY_API_TOKEN=your_apify_api_token
```

Add your own credentials. **Never commit `.env` or expose API keys in screenshots, logs, or public repositories.**

---

## 🚀 Run the Streamlit App

With the virtual environment activated, run:

```bash
streamlit run app.py
```

Open the local URL printed in your terminal.

### 🔄 Application Workflow

1. 📤 Upload a PDF resume.
2. 📑 The application extracts text from the resume.
3. 🧠 OpenRouter generates the resume summary, skill-gap analysis, and career roadmap.
4. 🎯 The application generates job-search keywords based on the resume summary.
5. 🔎 Apify actors fetch job listings from LinkedIn and Naukri.
6. 💼 Review the recommended job listings and open their application links.

---

## 🤖 Run the MCP Server

The MCP server exposes the job-fetching functions over STDIO.

```bash
python mcp_server.py
```

The process may wait silently for an MCP client. This is expected for STDIO transport. Keep the process running while the client is connected.

### 🔧 Available MCP Tools

**`fetchlinkedin(search_query: str)`**

Fetches LinkedIn job listings for the supplied search query.

**`fetchnaukri(search_query: str)`**

Fetches Naukri job listings for the supplied search query.

### 🧪 Test with MCP Inspector

Run MCP Inspector:

```bash
npx -y @modelcontextprotocol/inspector
```

In the Inspector, add a local STDIO server with:

- **Transport:** `stdio (local process)`
- **Command:** Full path to your virtual environment's Python executable, for example `venv\Scripts\python.exe`.
- **Arguments:** Full path to `mcp_server.py`.
- **Working directory:** Project root, if the Inspector provides this field.

Connect to the server and open the **Tools** tab. You should see `fetchlinkedin` and `fetchnaukri`.

---

## 🔑 Configuration Notes

- The OpenRouter client is configured in `src/helper.py` using the OpenAI-compatible API base URL.
- The current configured model is `openai/gpt-4o`. Model availability and pricing depend on your OpenRouter account and provider availability.
- LinkedIn and Naukri job retrieval is handled by Apify actors configured in `src/job_api.py`.
- Apify actor runs can take longer than MCP Inspector's default tool-call timeout. An Inspector timeout does not necessarily mean the Apify run failed; check the run status and logs in Apify.
- LinkedIn may rate-limit or reject scraping requests. Actor duration and returned results can vary.

---

## 📦 Dependencies

The project's `requirements.txt` includes:

```text
streamlit
openai
pymupdf
python-dotenv
apify-client
mcp[cli]<2
```

---

## 🔐 Security

- Store credentials only in your local `.env` file.
- Ensure `.env` is listed in `.gitignore`.
- Never commit API keys or tokens to GitHub.
- If a credential is accidentally exposed, revoke or rotate it in the provider dashboard and update your local `.env`.

---

## 🔮 Future Improvements

- ⚡ Improve handling of long-running Apify jobs and MCP request timeouts.
- 🎛️ Add configurable job-search locations, result counts, and filters.
- 🧹 Add job-result filtering and duplicate removal.
- 🧪 Add automated tests for resume parsing, API integrations, and MCP tools.
- 📊 Add job matching scores based on resume skills and job descriptions.

---

## 👩‍💻 Author

**Mousumi Badyakar**

---

⭐ If you find this project interesting, consider giving the repository a star!