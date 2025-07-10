# HTMX + FastAPI Tutorial Series

An educational tutorial project exploring modern web development with **minimal JavaScript** using HTMX and FastAPI.

## 🎥 Video Tutorials

Follow along with the complete video series on YouTube:

**[📺 HTMX + FastAPI Playlist](https://www.youtube.com/playlist?list=PLxvyAnoL-vu4JbdggUBrypf2lGKL-_MmC)**

## 🏗️ Architecture Philosophy

This tutorial series challenges conventional web development approaches by focusing on **server-side rendering** with minimal client-side JavaScript. Instead of building separate frontend and backend applications, we serve HTML directly from FastAPI with dynamic interactions powered by HTMX.

### Why This Approach?

- **Simpler Development**: No need for complex build tools, bundlers, or state management
- **Better Performance**: Smaller JavaScript bundles, faster initial page loads
- **SEO & AI Friendly**: Server-rendered HTML is immediately crawlable by search engines and readable by LLMs
- **Progressive Enhancement**: Works without JavaScript, enhanced with HTMX
- **Developer Experience**: Single codebase, familiar Python ecosystem

### AI/LLM Compatibility

This server-side rendering approach is particularly beneficial for AI and LLM consumption:

- **Structured Content**: Clean HTML markup provides clear content structure for LLMs
- **No JavaScript Dependencies**: Content is immediately available without client-side execution
- **Semantic HTML**: Proper HTML semantics help LLMs understand content hierarchy
- **Accessible by Design**: Content that works without JavaScript is inherently more accessible to AI systems

## 🛠️ Technology Stack

### Core Technologies

- **[HTMX](https://htmx.org/)**: Controversial architecture that replaces JavaScript-heavy frontends with server-side HTML updates
- **[FastAPI](https://fastapi.tiangolo.com/)**: Modern Python web framework with async-first design, making asynchronous development more straightforward compared to Django's synchronous origins.
- **[SSE (Server-Sent Events)](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)**: Real-time updates using `sse_starlette`
- **[Ollama](https://ollama.ai/)**: Local LLM integration with streaming responses

### Frontend & Styling

- **[Tailwind CSS](https://tailwindcss.com/)**: Controversial utility-first CSS framework with inline styling
- **[Jinja2](https://jinja.palletsprojects.com/)**: Python templating engine for dynamic HTML generation

### HTTP & Networking

- **[httpx](https://www.python-httpx.org/)**: Asynchronous HTTP client (async alternative to requests)

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Ollama (for LLM features)

### Installation

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd htmx
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install fastapi uvicorn httpx jinja2 sse-starlette
   ```

4. Start the development server:
   ```bash
   uvicorn fastapi_intro:app --reload
   ```

5. Open your browser to `http://localhost:8000`

## 📁 Project Structure

```
htmx/
├── fastapi_intro.py      # Basic FastAPI + HTMX example
├── 1_fastapi_intro/      # Tutorial episode 1 files
├── venv/                 # Python virtual environment
├── .gitignore           # Git ignore rules
└── README.md           # This file
```

## 🎯 Tutorial Episodes

Each episode builds upon the previous, introducing new concepts and technologies:

1. **FastAPI Introduction** - Basic setup and HTML serving
2. **HTMX Basics** - Dynamic content updates without JavaScript
3. **Server-Sent Events** - Real-time streaming with SSE
4. **Ollama Integration** - Local LLM with streaming responses
5. **Advanced Patterns** - Complex interactions and state management

## 🔄 Alternative to Modern Frontend

This approach offers a compelling alternative to traditional JavaScript-heavy architectures:

| Traditional Approach | HTMX + FastAPI Approach |
|---------------------|-------------------------|
| React/Vue + API | FastAPI serving HTML |
| Client-side state management | Server-side state |
| Complex build pipeline | Simple Python server |
| Large JavaScript bundles | Minimal client-side JS |
| Separate frontend/backend | Unified codebase |

## 🤝 Contributing

This is an educational project. Feel free to:

- Ask questions in the YouTube comments
- Fork and experiment with the code
- Share your own HTMX + FastAPI projects on YouTube

## 📚 Additional Resources

- [HTMX Documentation](https://htmx.org/docs/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Tailwind CSS Documentation](https://tailwindcss.com/docs)
- [Jinja2 Template Designer Documentation](https://jinja.palletsprojects.com/en/3.1.x/templates/)

## 📄 License

This project is for educational purposes. Feel free to use the code and concepts in your own projects.

## Oppkey Notes

- [Django vs FastAPI](docs/djangjo-vs-fastapi.md)

---

**Happy coding with minimal JavaScript! 🚀**
