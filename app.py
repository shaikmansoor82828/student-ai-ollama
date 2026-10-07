from flask import Flask, render_template, request
import ollama

app = Flask(__name__)
MODEL = "gemma3:1b"

def build_prompt(question, mode):
    prompts = {
        "ask": f"""You are an educational AI assistant.
Answer the student's question clearly and accurately.
Use simple English and give examples when useful.

Student question:
{question}""",
        "study": f"""You are a Student AI Study Assistant.
Help the student understand this academic topic.
Use simple English, important points, and a small example.

Topic:
{question}""",
        "simple": f"""You are a Student AI assistant.
Explain the following academic topic in very simple English.
Use easy words and one simple example.

Topic:
{question}""",
        "notes": f"""You are a Student AI Notes Assistant.
Create short, useful study notes.

Include:
- Definition
- Important points
- Example
- Key terms

Use simple English.

Topic:
{question}""",
        "mistake": f"""You are a Student AI Mistake Explainer.
Analyze the student's answer and explain:
1. What is wrong
2. Why it is wrong
3. The correct explanation
4. One tip to avoid the mistake

Be encouraging and use simple English.

Student's answer:
{question}""",
        "compare": f"""You are a Student AI Comparison Assistant.
Compare the two academic concepts.

Include:
1. Definition of each
2. Main differences
3. Similarities
4. A simple comparison table
5. Short conclusion

Use simple English.

Concepts:
{question}"""
    }
    return prompts.get(mode, prompts["ask"])

@app.route("/", methods=["GET", "POST"])
def home():
    answer = ""
    question = ""
    mode = "ask"

    if request.method == "POST":
        question = request.form.get("question", "").strip()
        mode = request.form.get("mode", "ask")

        if not question:
            answer = "Please enter a topic or question."
        else:
            try:
                response = ollama.generate(
                    model=MODEL,
                    prompt=build_prompt(question, mode)
                )
                answer = response["response"].strip()
            except Exception as error:
                print("Ollama error:", error)
                answer = (
                    "Unable to connect to Ollama. Make sure Ollama is running "
                    f"and that the '{MODEL}' model is installed."
                )

    return render_template(
        "index.html",
        question=question,
        answer=answer,
        mode=mode
    )

if __name__ == "__main__":
    app.run(debug=True)
