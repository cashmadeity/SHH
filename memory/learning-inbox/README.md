# Learning Inbox

Raw information captured from external sources (YouTube, articles, etc.) waiting for evaluation and implementation.

## Structure

```
learning-inbox/
├── inbox/              # Raw captures (not yet processed)
│   ├── video-*.json    # Extracted concepts from videos
│   ├── article-*.json  # Web articles
│   └── raw-*.json      # Anything else
├── staging/            # Evaluated, ready for review
│   ├── approved-*.json # Passed evaluation
│   └── rejected-*.json # Failed eval, but logged
├── implemented/        # Integrated into MEMORY.md
└── evaluation-log.json # Decision history
```

## Workflow

1. **CAPTURE** → inbox/ (automatic from youtube-learner.js)
2. **EVALUATE** → Batch review, scoring
3. **STAGE** → staging/approved/ (ready to use)
4. **IMPLEMENT** → MEMORY.md (integrate into long-term memory)
5. **LOG** → evaluation-log.json (track decisions)

## Example Entry

```json
{
  "id": "video-MtzLiQ9w1c",
  "source": "youtube",
  "title": "Machine Learning Fundamentals",
  "raw_concepts": ["supervised learning", "neural networks", ...],
  "timestamp": "2026-03-23T02:32:23Z",
  "status": "inbox",
  "confidence": 0.85,
  "relevance_to_user": "medium",
  "ready_to_use": false,
  "eval_notes": "Waiting for batch review"
}
```

## Evaluation Criteria

- **Relevance:** How useful for understanding Cash's work/preferences?
- **Accuracy:** Is the info correct/reliable?
- **Actionability:** Can I actually use this to improve?
- **Redundancy:** Already know this?
- **Integration:** Where does it fit in MEMORY.md?

---

**Status:** Inbox system ready  
**Last Updated:** 2026-03-23 02:36 UTC
