# Student AI — Local Ollama Study Assistant

A clean local AI study assistant built with **Python, Flask, Ollama, and Gemma 3 1B**.

Student AI supports question answering, study help, simple explanations, revision notes, mistake explanations, and concept comparisons. The language model runs locally through Ollama, so this project does not require a cloud AI API key.

## Features

- Ask AI
- Study Help
- Explain Simply
- Notes Helper
- Mistake Explainer
- Compare Concepts
- Copy generated answers
- Responsive web interface
- Local AI with Ollama
- Configurable Ollama model using OLLAMA_MODEL

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Application logic |
| Flask | Web framework |
| Ollama | Local AI runtime |
| Gemma 3 1B | Local language model |
| HTML / CSS / JavaScript | User interface |

## Project Structure

student-ai-ollama/
- app.py
- requirements.txt
- .gitignore
- README.md
- templates/index.html
- static/style.css

## Run Locally

### 1. Clone

    git clone https://github.com/shaikmansoor82828/student-ai-ollama.git
    cd student-ai-ollama

### 2. Create a virtual environment

Windows:

    python -m venv venv
    venv\\Scripts\\activate

### 3. Install dependencies

    pip install -r requirements.txt

### 4. Install the Ollama model

    ollama pull gemma3:1b
    ollama list

Make sure Ollama is running before starting Flask.

### 5. Start the application

    python app.py

Open http://127.0.0.1:5000 in your browser.

## Optional Model Configuration

The default model is gemma3:1b.

Windows PowerShell:

    $env:OLLAMA_MODEL="your-model-name"
    python app.py

macOS / Linux:

    export OLLAMA_MODEL="your-model-name"
    python app.py

## How It Works

Student
→ Flask Web Interface
→ Select Study Mode
→ Prompt Builder
→ Ollama
→ Gemma 3 1B
→ Generated Answer

Each mode uses a focused prompt before sending the request to the local model.

## Privacy

The project is designed for local AI usage. Prompts are sent to the Ollama service running on your computer rather than to a cloud AI API configured by this project.

## Limitations

Gemma 3 1B is a small local model. It is lightweight and useful for basic study assistance, but larger models can provide more detailed responses.

## Future Improvements

- Chat history
- Streaming responses
- PDF and document Q&A
- Retrieval-Augmented Generation (RAG)
- Voice input
- Dark mode
- User accounts
- Automated tests
- Deployment configuration

## Author

**Shaik Mansoor**

GitHub: https://github.com/shaikmansoor82828
