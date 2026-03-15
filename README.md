---

# LLD Validator — UML Class Diagram Analysis with Multi-Agent AI

An intelligent Low Level Design (LLD) validation system that automatically analyzes UML Class Diagrams using a **multi-agent AI pipeline** built with [CrewAI](https://github.com/crewAIInc/crewAI) and locally hosted LLMs via [Ollama](https://ollama.com).

## Overview

Designing a clean, maintainable system architecture is hard. This tool automates the review process by running your UML Class Diagram through a team of specialized AI agents — each responsible for a different layer of analysis — and produces a structured evaluation report with scores, explanations, and actionable improvement tips.

Instead of manually reviewing class diagrams for structural issues, broken relationships, or SOLID violations, you simply provide the diagram and the agents do the rest.

## How It Works

The system uses a **hierarchical multi-agent architecture** orchestrated by a manager agent that coordinates four specialized validators in sequence:

```
UML Class Diagram Input
        ↓
Structural Validator       →  validates classes, attributes, methods, interfaces
        ↓
Relationship Validator     →  validates associations, inheritance, composition, patterns
        ↓
Design Quality Analyzer    →  evaluates SOLID principles, coupling, cohesion, smells
        ↓
Feedback Evaluator         →  aggregates all outputs → final JSON evaluation report
```

## Features

- **Structural Validation** — checks class definitions, visibility modifiers, attribute types, method signatures, and interface correctness
- **Relationship Validation** — verifies associations, aggregations, compositions, inheritance hierarchies, multiplicity, and cyclic dependencies
- **Design Pattern Detection** — automatically identifies Creational, Structural, and Behavioral GoF patterns present in the diagram
- **SOLID Principle Analysis** — flags violations of SRP, OCP, LSP, ISP, and DIP
- **Design Smell Detection** — detects God Classes, Feature Envy, Data Classes, and cyclic dependencies
- **Architecture Layer Validation** — checks separation of Controller, Service, Repository, and Domain layers
- **Scored Evaluation Report** — produces a final JSON report with per-dimension scores and an overall design score
- **Improvement Recommendations** — generates concrete, actionable tips to fix identified issues
- **Fully Local** — runs entirely on your machine using Ollama, no external API calls required

## Tech Stack

| Component | Technology |
|-----------|------------|
| Agent Framework | [CrewAI](https://github.com/crewAIInc/crewAI) |
| LLM Backend | [Ollama](https://ollama.com) (local) |
| Inference Models | `qwen3-coder:480b-cloud` |
| Embedding Model | `qwen3-embedding:0.6b` |
| Vector Memory | ChromaDB via RAGStorage |
| Long-term Memory | SQLite via LTMSQLiteStorage |
| Language | Python 3.13 |
| Package Manager | uv |

## Output

The final report is a structured JSON file containing:

```json
{
  "score": {
    "structural_validation": 85,
    "relationship_validation": 70,
    "design_quality": 65,
    "design_patterns": 50,
    "solid_principles": 60,
    "coupling_cohesion": 72,
    "architecture_layering": 55,
    "overall_score": 65
  },
  "description": "...",
  "improvement": {
    "improvement_tips": ["..."]
  }
}
```

Intermediate markdown reports from each agent are also saved to the `output/` directory for detailed inspection.

---

