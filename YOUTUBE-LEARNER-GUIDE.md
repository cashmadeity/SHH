# YouTube Learner System

Learn from YouTube videos. Extract concepts. Use in agent responses.

## Quick Start

### 1. Learn from a Video

```bash
node youtube-learner.js "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
```

Output:
- Extracts transcript
- Identifies concepts via LLM
- Stores in `memory/youtube-learned/`
- Updates knowledge index

### 2. Search Learned Content

```python
from youtube_retriever import YouTubeRetriever

retriever = YouTubeRetriever()

# Search for concepts
results = retriever.search("machine learning", top_k=3)

# Get context for agent response
context = retriever.get_context("AI")
```

### 3. Use in Agent Responses

```python
# In your agent code:
from youtube_retriever import YouTubeRetriever

retriever = YouTubeRetriever()

def respond_to_user(query):
    context = retriever.get_context(query)
    
    # Add context to response
    response = f"Based on what I've learned:\n{context}\n\nNow, to answer your question..."
    
    return response
```

## System Components

### youtube-learner.js
- **Input:** YouTube URL
- **Process:** Fetch transcript → Extract via LLM → Store
- **Output:** JSON with concepts, takeaways, vocabulary
- **Dependencies:** `yt-dlp`, Node.js, OpenRouter API

### youtube-retriever.py
- **Input:** Search query
- **Process:** Search index → Rank by relevance → Format context
- **Output:** Context string for agent insertion
- **Dependencies:** Python 3.6+

### Memory Structure

```
memory/
├── youtube-learned/
│   ├── dQw4w9WgXcQ.json    (video concepts)
│   ├── <video_id>.json
│   └── ...
└── youtube-index.json      (master index for fast search)
```

## Example Output

**Input:** `https://www.youtube.com/watch?v=XYZ123`

**Extracted Concepts:**
```json
{
  "title": "Introduction to Machine Learning",
  "key_concepts": [
    "supervised learning",
    "neural networks",
    "gradient descent",
    "backpropagation"
  ],
  "main_takeaways": [
    "ML requires labeled data for training",
    "Neural networks learn through iterative optimization"
  ],
  "vocabulary": ["algorithm", "model", "training", "prediction", ...],
  "summary": "This video covers the fundamentals of machine learning, focusing on supervised learning and how neural networks use backpropagation to optimize weights."
}
```

**Agent Context Insertion:**
```
From my YouTube learning:
- Introduction to Machine Learning: supervised learning, neural networks, gradient descent
```

## Configuration

API key stored in: `/root/.openclaw/credentials/openrouter.env`

```
OPENROUTER_API_KEY=sk-or-v1-...
OPENROUTER_MODEL=meta-llama/llama-3-70b-instruct
```

## Rate Limits

- OpenRouter: Check your plan limits
- yt-dlp: No limits (local)
- Storage: Unlimited (stored locally)

## Troubleshooting

### "Invalid YouTube URL"
- Ensure URL is in format: `youtube.com/watch?v=...` or `youtu.be/...`

### "Could not fetch transcript"
- Video must have captions enabled
- Try another video

### "OpenRouter error"
- Check API key validity
- Verify rate limits not exceeded
- Check OpenRouter account credits

## Privacy

- All transcripts downloaded locally
- No data sent to third parties (except OpenRouter LLM calls)
- Concepts stored in `memory/` (git-backed up)

## Future Enhancements

- [ ] Vector embeddings for semantic search
- [ ] Multi-language transcript support
- [ ] Automatic YouTube playlist learning
- [ ] Sentiment analysis of video content
- [ ] Integration with agent personality learning

---

**Status:** Production-ready  
**Last Updated:** 2026-03-23  
**Maintained by:** Cash
