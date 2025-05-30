# Website_GPT_Bot_Widget
# 💬 Website ChatGPT Chatbot Widget

Bring your website to life with a powerful, intelligent chatbot powered by **GPT-3.5 Turbo via OpenRouter API**.  
Easily integrate using `<iframe>` or `<script>` — no complex setup needed!

---

## ✨ Features

- ⚡ Real-time conversation powered by ChatGPT (via OpenRouter)
- 🧠 Uses GPT-3.5 Turbo for fast & intelligent replies
- 🌐 Simple HTML + Python (Flask) backend
- 🔒 API key integration (your key remains private)
- 🔌 Easy to embed with `<iframe>` or custom script
- 📱 100% Mobile responsive

---

## 🛠️ How It Works

📁 project/
├── app.py → Flask backend for handling requests
├── widget.html → Frontend chatbot widget
├── static/
│ └── style.css → Optional styling file


---

## 🚀 How to Run Locally

1. **Clone the repository**  
   
   git clone https://github.com/Imdad990/Website_GPT_widget.git
   cd chatgpt-widget
Install dependencies
pip install flask requests
Update your API key in app.py

python
OPENROUTER_API_KEY = "your_openrouter_key_here"
Run the app
python app.py
Open widget.html in browser

🔌 Embed on Any Website
html
<iframe src="https://yourdomain.com/widget.html" 
        width="100%" height="500px" style="border:none;">
</iframe>
🧠 Use Cases
Customer support bots

24/7 visitor assistance

Sales inquiry assistant

Educational websites

AI demo for clients

📦 Deployment Options
🔗 Netlify

🐍 PythonAnywhere

🟣 Vercel (via frontend-only mode)

🔒 API Key Safety
⚠️ Important: Never share your OpenRouter API key publicly.
Use environment variables or secret management if deploying online.

🤝 Let's Collaborate
Need help customizing this chatbot for your business?
Reach out on LinkedIn or hire me on Fiverr.

