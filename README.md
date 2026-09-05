# Vignesh AI Assistant – Voice FAQ Bot

A simple AI-powered FAQ assistant that allows users to ask questions using **text or voice** and receive intelligent answers.

## 🚀 Features

* 🎤 Voice input
* ⌨️ Text input
* 🤖 AI-powered question answering
* 🔊 Voice response support
* 📚 FAQ-based question answering
* ⚡ Simple and interactive Streamlit interface
* 🔐 API key stored securely using environment variables
* ❌ Basic error handling for invalid or unavailable API requests

## 🧩 How the System Works

```text
User
  │
  ├── Text Question
  │
  └── Voice Question
          │
          ▼
     Speech-to-Text
          │
          ▼
      AI Assistant
          │
          ▼
     Answer Generation
          │
          ▼
     Text Response
          │
          ▼
     Voice Response
```

## 🛠️ Technologies Used

* **Python**
* **Streamlit**
* **Google Gemini API**
* **Speech-to-Text**
* **Text-to-Speech**
* **python-dotenv**
* **Git & GitHub**

## 📁 Project Structure

```text
vignesh-ai-assistant/
│
├── app.py
├── faq.json
├── requirements.txt
├── .gitignore
├── README.md
└── .env
```

> **Note:** `.env` is used only for local development and should not be uploaded to GitHub.

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/vikivicki/vignesh-ai-assistant.git
```

### 2. Open the project folder

```bash
cd vignesh-ai-assistant
```

### 3. Create a virtual environment

Windows:

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

For macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

## 🔑 API Key Configuration

The application requires a Google Gemini API key.

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your actual API key.

### Important Security Rule

**Never upload your real API key to GitHub.**

Add the following to `.gitignore`:

```text
.env
venv/
__pycache__/
*.pyc
```

If an API key has already been pushed to GitHub, revoke it and create a new key.

## ▶️ Run the Application

Start the Streamlit application with:

```bash
streamlit run app.py
```

The application will open in your browser.

## 💬 Example

A user can enter a question such as:

```text
What services does the assistant provide?
```

The application processes the question and returns an AI-generated answer.

Users can also use the voice input option when available.

## 📚 FAQ Knowledge Base

The project can use an FAQ knowledge base to provide relevant information to users.

Example structure:

```json
[
  {
    "question": "Example question",
    "answer": "Example answer"
  }
]
```

The FAQ content can be updated according to the requirements of the project.

## 🧪 Testing

Before deployment, test the following:

* Text input
* Voice input
* AI response generation
* Voice response
* Invalid questions
* Missing API key
* Invalid API key
* Internet/API connection errors
* Application startup

## ☁️ Deployment

The application can be deployed using a Streamlit-compatible hosting platform.

For deployment:

1. Push the project files to GitHub.
2. Connect the repository to the hosting platform.
3. Configure the required API key using the platform's **Secrets/Environment Variables** section.
4. Do **not** upload the `.env` file containing the real API key.
5. Start the application using:

```bash
streamlit run app.py
```

## 🔐 Security

API credentials should be stored using environment variables or the hosting platform's secret-management system.

Do not hard-code API keys inside `app.py`.

Do not commit the following files to GitHub:

```text
.env
```

## ⚠️ Known Limitations

* Voice functionality depends on the user's browser/device and available audio permissions.
* AI responses depend on the availability of the configured API.
* Internet connectivity is required for cloud-based AI services.
* Speech recognition may vary depending on microphone quality and background noise.

## 🎯 Project Objective

The objective of this project is to build a simple and user-friendly AI FAQ assistant that supports both **text and voice interaction**.

It demonstrates the integration of:

* Artificial Intelligence
* Natural Language Processing
* Speech interaction
* API integration
* Streamlit web applications

## 🤖 AI Assistance

AI tools may be used during development for debugging, code assistance, documentation, and improving the project workflow.

## 📌 Conclusion

**Vignesh AI Assistant** demonstrates how an AI-powered FAQ system can be combined with text and voice interaction to create an accessible and interactive user experience.

The project can be further extended with additional FAQ data, improved speech processing, authentication, conversation history, and other AI features.

## 👨‍💻 Author

**Vignesh**

GitHub:
https://github.com/vikivicki/vignesh-ai-assistant
