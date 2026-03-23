#!/usr/bin/env python3
"""
YOUTUBE RETRIEVER - Search & retrieve learned YouTube concepts in agent responses
"""

import json
import os
from pathlib import Path
from typing import List, Dict, Optional

class YouTubeRetriever:
    def __init__(self, memory_dir="memory/youtube-learned"):
        self.memory_dir = Path(memory_dir)
        self.index_path = Path("memory/youtube-index.json")
        self.index = self._load_index()

    def _load_index(self) -> Dict:
        """Load the master knowledge index"""
        if self.index_path.exists():
            with open(self.index_path) as f:
                return json.load(f)
        return {}

    def search(self, query: str, top_k: int = 3) -> List[Dict]:
        """
        Search learned YouTube concepts by keyword
        
        Returns:
            List of relevant concept entries, ranked by relevance
        """
        query_words = set(query.lower().split())
        results = []

        for video_id, entry in self.index.items():
            relevance = 0
            concepts = entry.get('concepts', [])
            
            # Score based on keyword overlap
            for concept in concepts:
                concept_words = set(concept.lower().split())
                overlap = len(query_words & concept_words)
                if overlap > 0:
                    relevance += overlap
            
            if relevance > 0:
                results.append({
                    'video_id': video_id,
                    'title': entry.get('title', 'Unknown'),
                    'concepts': concepts,
                    'relevance': relevance,
                    'timestamp': entry.get('timestamp'),
                })

        # Sort by relevance
        results.sort(key=lambda x: x['relevance'], reverse=True)
        return results[:top_k]

    def get_context(self, query: str) -> str:
        """
        Get formatted context string for agent insertion
        
        Usage in agent response:
            context = retriever.get_context("machine learning")
            response = f"Based on what I've learned: {context}\n\n{original_response}"
        """
        results = self.search(query, top_k=2)
        
        if not results:
            return ""

        context_lines = ["From my YouTube learning:"]
        for result in results:
            context_lines.append(f"- {result['title']}: {', '.join(result['concepts'][:3])}")
        
        return "\n".join(context_lines)

    def list_all(self) -> Dict:
        """List all learned videos"""
        return self.index

    def get_video_details(self, video_id: str) -> Optional[Dict]:
        """Get full details for a specific video"""
        video_path = self.memory_dir / f"{video_id}.json"
        if video_path.exists():
            with open(video_path) as f:
                return json.load(f)
        return None

# ============================================================================
# Quick test
# ============================================================================

if __name__ == "__main__":
    retriever = YouTubeRetriever()
    
    print("📚 YouTube Knowledge Base")
    print(f"Videos learned: {len(retriever.list_all())}")
    
    # Test search
    test_query = "learning"
    results = retriever.search(test_query)
    print(f"\nSearch results for '{test_query}':")
    for r in results:
        print(f"  - {r['title']}: {r['concepts']}")
    
    # Test context insertion
    print(f"\nContext for agent:\n{retriever.get_context(test_query)}")
