# Wikipedia Search & Summarizer

A Flask web application that allows users to search Wikipedia articles and get AI-powered summaries of the content.

## Features

- **Wikipedia Search**: Search for articles using the Wikipedia API
- **AI Summarization**: Get concise summaries of Wikipedia articles using OpenAI-compatible models
- **Modern UI**: Clean, responsive web interface with glassmorphism design
- **REST API**: JSON API endpoints for search and summarization

## Project Structure

```
first_flask_app/
  wikisearch/           # Main application package
    __init__.py      # Flask app factory
    search.py        # Wikipedia search API endpoint
    summarize.py     # AI summarization endpoint
    inference.py     # AI model inference utilities
    prompts.py       # AI prompt templates
  wsgi.py              # WSGI entry point
  index.html           # Frontend web interface
  pyproject.toml       # Python project configuration
  README.md           # This file
```

## Requirements

- Python 3.12+
- OpenAI-compatible API (OpenAI, Azure OpenAI, local models, etc.)
- Environment variables for AI model configuration

## Installation

1. Install dependencies using uv:
```bash
uv sync
```

2. Set up environment variables by creating a `.env` file:
```bash
BASE_URL=https://api.openai.com/v1  # or your AI provider's URL
API_KEY=your_api_key_here
MODEL_ID=gpt-3.5-turbo  # or your preferred model
```

## Usage

### Running the Application

Start the Flask development server:
```bash
python wsgi.py
```

The application will be available at http://127.0.0.1:5000

### API Endpoints

#### Search Wikipedia
- **URL**: `/api/search`
- **Method**: POST
- **Body**: `{"term": "search term"}`
- **Response**: `{"results": ["Article 1", "Article 2", ...]}`

#### Summarize Article
- **URL**: `/api/summarize`  
- **Method**: POST
- **Body**: `{"title": "Wikipedia Article Title"}`
- **Response**: `{"summary": "AI-generated summary..."}`

### Web Interface

Open `index.html` in your browser or serve it alongside the Flask app. The interface provides:

1. Search box to find Wikipedia articles
2. Clickable search results
3. AI-generated summaries displayed in a separate panel

## Dependencies

- **Flask**: Web framework and API
- **flask-cors**: Cross-origin request handling
- **wikipedia**: Wikipedia API client
- **openai**: OpenAI API client (works with compatible APIs)
- **python-dotenv**: Environment variable management
- **mypy**: Static type checking

## Development

The project uses MyPy for type checking with strict mode enabled. Run type checking with:
```bash
mypy wikisearch/
```

## Configuration

The application requires these environment variables:
- `BASE_URL`: AI model API base URL
- `API_KEY`: AI model API key
- `MODEL_ID`: AI model identifier

## Architecture

- **Frontend**: Pure HTML/CSS/JavaScript with modern styling
- **Backend**: Flask with Blueprint-based organization
- **AI Integration**: OpenAI-compatible API for text summarization
- **Wikipedia Integration**: Official Wikipedia Python library