# Student AI — Local Ollama Assistant

A beginner-friendly AI study assistant built with **Python, Flask, Ollama, and Gemma 3 1B**. The AI runs locally on your computer, so no Gemini/OpenAI API key is required.

## Features

- Ask AI
- Study Help
- Explain Simply
- Notes Helper
- Mistake Explainer
- Compare Concepts
- Copy AI answers
- Clear input
- Responsive web interface
- Local AI with Ollama

## Project Structure

```text
student-ai-ollama/
├── app.py
├── requirements.txt
├── .gitignore
├── README.md
├── templates/
│   └── index.html
└── static/
    └── style.css
```

## Requirements

- Python 3.10 or newer
- Ollama
- Gemma 3 1B model

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/shaikmansoor82828/student-ai-ollama.git
cd student-ai-ollama
```

### 2. Create a virtual environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Python packages

```bash
pip install -r requirements.txt
```

### 4. Install the local AI model

```bash
ollama pull gemma3:1b
```

Check it:

```bash
ollama list
```

### 5. Start the Flask app

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

## Architecture

```text
Student
   ↓
Flask Web Interface
   ↓
Selected AI Mode
   ↓
Prompt Builder
   ↓
Ollama Local API
   ↓
Gemma 3 1B
   ↓
AI Answer
```

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Application logic |
| Flask | Web framework |
| Ollama | Local AI runtime |
| Gemma 3 1B | Local language model |
| HTML/CSS/JavaScript | User interface |

## Important Note

Gemma 3 1B is a small local model. It is fast and useful for basic study tasks, but its answers may be less detailed or accurate than larger cloud models.

## Future Improvements

- Chat history
- User login
- PDF/document Q&A
- RAG
- Voice input
- Dark mode
- Streaming AI responses

## Author

**Shaik Mansoor**
