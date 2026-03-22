#!/usr/bin/env python3
"""
LEARN FROM BASE - Agent learns vocabulary and response patterns from base.txt locally
Builds a knowledge model without external APIs
"""

import json
import re
from pathlib import Path

def learn_from_file(filename):
    """Read base.txt and extract knowledge patterns"""
    
    with open(filename, 'r') as f:
        content = f.read()
    
    # Split by chapters
    chapters = re.split(r'Chapter \d+:', content)
    
    knowledge = {
        "key_concepts": [],
        "response_patterns": [],
        "chapter_summaries": [],
        "vocabulary": set(),
        "questions_and_answers": []
    }
    
    for chapter in chapters[1:]:  # Skip empty first split
        lines = chapter.strip().split('\n')
        title = lines[0].strip() if lines else "Unknown"
        
        # Extract key concepts (first sentence of each paragraph)
        paragraphs = [p.strip() for p in chapter.split('\n\n') if p.strip()]
        
        for para in paragraphs[:2]:  # First 2 paragraphs per chapter
            sentences = re.split(r'[.!?]+', para)
            if sentences:
                concept = sentences[0].strip()
                if len(concept) > 20:
                    knowledge["key_concepts"].append({
                        "chapter": title,
                        "concept": concept
                    })
        
        # Extract all words for vocabulary
        words = re.findall(r'\b[a-z]+\b', chapter.lower())
        knowledge["vocabulary"].update(words)
        
        # Generate response patterns
        knowledge["response_patterns"].append({
            "topic": title,
            "summary": ' '.join(paragraphs[0].split()[:30])  # First 30 words
        })
    
    # Convert set to list for JSON
    knowledge["vocabulary"] = sorted(list(knowledge["vocabulary"]))
    
    return knowledge

# Learn from base.txt
print("Learning from base.txt...")
learned = learn_from_file('base.txt')

# Save learned knowledge
with open('learned_knowledge.json', 'w') as f:
    json.dump(learned, f, indent=2)

print(f"\nLearning Complete!")
print(f"- Key concepts extracted: {len(learned['key_concepts'])}")
print(f"- Vocabulary words learned: {len(learned['vocabulary'])}")
print(f"- Response patterns: {len(learned['response_patterns'])}")
print(f"\nSample concepts:")
for concept in learned['key_concepts'][:3]:
    print(f"  - {concept['chapter']}: {concept['concept'][:80]}...")

print(f"\nSample vocabulary (first 20 words):")
print(f"  {', '.join(learned['vocabulary'][:20])}")

print("\nKnowledge saved to: learned_knowledge.json")
print("Agent can now reference this locally without APIs.")
