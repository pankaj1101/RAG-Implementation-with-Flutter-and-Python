# RAG Implementation with Flutter & Python

A Retrieval-Augmented Generation (RAG) application built using Flutter for the frontend and Python (FastAPI) for the backend. The application retrieves relevant information from web sources and uses LLMs to generate context-aware responses.

## Features

* Flutter mobile application
* FastAPI backend
* Web search integration using Tavily
* Content extraction using Trafilatura
* Retrieval-Augmented Generation (RAG)
* REST API communication
* Environment variable configuration
* Modular architecture

---

## Project Structure

```text
rag_impl/
│
├── flutter_app/
│   ├── lib/
│   ├── android/
│   ├── ios/
│   └── pubspec.yaml
│
├── server/
│   ├── main.py
│   ├── config.py
│   ├── services/
│   │   └── search_service.py
│   ├── requirements.txt
│   └── .env
│
└── README.md
```

---

## Backend Setup

### 1. Clone Repository

```bash
git clone https://github.com/pankaj1101/RAG-implementation-Flutter-With-Python.git
cd RAG-implementation-Flutter-With-Python
```

### 2. Create Virtual Environment

```bash
cd server

python3 -m venv venv
```

### 3. Activate Virtual Environment

#### macOS / Linux

```bash
source venv/bin/activate
```

#### Windows

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Create Environment File

Create a `.env` file inside the `server` folder:

```env
TAVILY_API_KEY=your_tavily_api_key
```

---

## Run Backend

```bash
uvicorn main:app --reload
```

Server will start at:

```text
http://127.0.0.1:8000
```

Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

---

## API Endpoint

### Chat API

**POST**

```http
/api/chat
```

#### Request

```json
{
  "query": "What is Retrieval Augmented Generation?"
}
```

#### Response

```json
[
  {
    "title": "Sample Article",
    "url": "https://example.com",
    "content": "Retrieved content..."
  }
]
```

---

## Flutter Setup

Navigate to Flutter project:

```bash
cd flutter_app
```

Install packages:

```bash
flutter pub get
```

Run application:

```bash
flutter run
```

---

## Technologies Used

### Frontend

* Flutter
* Dart

### Backend

* Python
* FastAPI
* Tavily Search API
* Trafilatura
* Uvicorn

### AI / RAG

* LLM Integration
* Web Search Retrieval
* Context Extraction

---

## Environment Variables

| Variable       | Description           |
| -------------- | --------------------- |
| TAVILY_API_KEY | Tavily Search API Key |

---

## Ignored Files

The following files are intentionally excluded from Git:

```gitignore
server/.env
server/venv/
android/app/release/
```

---

## Future Enhancements

* Vector database integration
* Semantic search
* Chat history
* User authentication
* Multi-model support
* Streaming responses
* Citation support

---

## Author

Pankaj Ram

Cross-Platform Mobile App Developer

GitHub: https://github.com/pankaj1101
GitHub Repository: https://github.com/pankaj1101/RAG-Implementation-Flutter-With-Python
