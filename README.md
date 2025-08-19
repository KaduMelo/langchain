Here’s the full translation into English:

---

# Introduction to LangChain

This course is intended for those who want to have their first contact with LangChain. Below, we present the instructions for setting up the environment using `venv`, installing the necessary dependencies, and an overview of the main topics covered.

## Environment Setup

To configure the environment and install the project dependencies, follow the steps below:

1. **Create and activate a virtual environment (`venv`):**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install the dependencies:**

   **Option A - From `requirements.txt`:**

   ```bash
   pip install -r requirements.txt
   ```

   **Option B - Direct installation of the main packages:**

   ```bash
   pip install langchain langchain-openai langchain-google-genai langchain-community langchain-text-splitters langchain-postgres psycopg[binary] python-dotenv beautifulsoup4 pypdf && pip freeze > requirements.txt
   ```

   This command will also automatically install all dependencies and generate the `requirements.txt` file.

3. **Set up environment variables:**

   * Duplicate the `.env.example` file and rename it to `.env`
   * Open the `.env` file and replace the values with your actual API keys obtained as instructed below

## Main Topics Covered

### Basic Fundamentals

* **Introduction to LangChain:** Basic concepts and first integration with language models
* **Integration with OpenAI:** How to use ChatOpenAI for basic interactions
* **Integration with Google Gemini:** Configuration and use of the Gemini model via Google GenAI
* **Prompt Templates:** Creating simple and advanced templates for prompts
* **Chat Prompts:** Implementing conversation systems with structured templates

### Chains and Advanced Processing

* **LCEL (LangChain Expression Language):** Pipe (|) syntax to connect components
* **Basic Chains:** Creating simple question-and-answer pipelines
* **Complex Chains:** Multi-step pipelines with translation and summarization
* **Custom Runnables:** @chain decorator and RunnableLambda for custom functions
* **Text Splitters:** Splitting long texts into chunks for processing
* **Summarization Chains:** "Stuff" and "map\_reduce" techniques for document summarization
* **Structured Output:** Extracting structured data using Pydantic models

### Agents and Tools

* **Custom Tools:** Creating custom tools with the @tool decorator
* **ReAct Agents:** Implementing agents that reason and act
* **Agent Executors:** Orchestrating agents with multiple tools
* **Prompt Hub:** Using community-provided predefined prompts

### Memory Management

* **Chat History:** Implementing persistent conversation history
* **Message Memory:** Storing and retrieving messages in sessions
* **Memory Trimming:** Sliding window techniques for managing limited context
* **Session Management:** Managing multiple conversation sessions

### Document Loaders and RAG

* **Web Loaders:** Loading content from web pages
* **PDF Loaders:** Processing and extracting text from PDF documents
* **Document Chunking:** Strategies for splitting documents for efficient processing
* **RAG Foundations:** Basic concepts for Retrieval-Augmented Generation

## Requirements to Run the Code

To run the code provided in the course, you must create API keys for the OpenAI and Google Gemini services. Below, we provide detailed instructions for creating these keys.

### Creating an API Key in OpenAI

1. **Go to the OpenAI website:**

   [https://platform.openai.com/account/api-keys](https://platform.openai.com/account/api-keys)

2. **Log in or create an account:**

   * If you already have an account, click "Log in" and enter your credentials.
   * Otherwise, click "Sign up" to create a new account.

3. **Navigate to the API Keys section:**

   * After logging in, click on "API Keys" in the left-hand menu.

4. **Create a new API Key:**

   * Click the "Create new secret key" button.
   * Give the key a name to identify it easily.
   * Click "Create secret key".

5. **Copy and store your API Key:**

   * The key will be displayed only once. Copy it and paste it into the `.env` file under the `OPENAI_API_KEY` variable.

For more details, see the full tutorial: [How to Generate an API Key in OpenAI?](https://hub.asimov.academy/tutorial/como-gerar-uma-api-key-na-openai/)

### Creating an API Key in Google Gemini

1. **Go to Google AI Studio:**

   [https://ai.google.dev/gemini-api/docs/api-key?hl=en](https://ai.google.dev/gemini-api/docs/api-key?hl=en)

2. **Log in with your Google account:**

   * Use your Google account to access AI Studio.

3. **Navigate to the API Keys section:**

   * In the dashboard, click on "API Keys".

4. **Create a new API Key:**

   * Click "Create API Key".
   * Give the key a name to identify it easily.
   * The key will be generated and displayed on the screen.

5. **Copy and store your API Key:**

   * Copy the generated key and paste it into the `.env` file under the `GOOGLE_API_KEY` variable.

For more information, check the official documentation: [How to Use Gemini API Keys](https://ai.google.dev/gemini-api/docs/api-key?hl=en)

**Note:** Make sure not to share your API keys publicly and store them in safe locations, as they grant access to the corresponding services.

---

Quer que eu também adapte esse texto para um **material didático em inglês** (com linguagem mais amigável e estilo de tutorial), ou prefere manter a tradução literal mais próxima do original?
