# no1homelab - The Genesis Agent

This repository contains the source code for **No. 1**, the main AI assistant for The Architect's Digital Empire.

## Mission

This agent's primary purpose is to act as a "Project Scaffolder" and a general-purpose assistant, embodying the principles and philosophies outlined in its [Identity Document](docs/AGENT_IDENTITY.md).

This project is the first step towards the development of a J.A.R.V.I.S.-like entity.

## Installation & Usage

This project uses a dedicated virtual environment (`ai_lab`).

1.  **Install dependencies:**

    ```bash
    # From within the no1homelab directory
    /home/clubsxno1/ai_lab/bin/pip install -e .
    ```

2.  **Run the agent:**

    ```bash
    # Use the installed entry point, providing a prompt
    /home/clubsxno1/ai_lab/bin/no1-scaffold "Your prompt for the agent"
    ```

## Current Status: Phase 1 Complete

-   **LLM Integration:** The agent is successfully integrated with a backend Ollama server running the `mixtral:8x7b` model on an Intel Arc GPU.
-   **Cognitive Flow:** The agent can receive a prompt, send it to the LLM for processing, and receive a raw text response.
-   **Next Steps:** The next phase involves implementing Retrieval-Augmented Generation (RAG) to provide the agent with memory and context from local documents, and re-enabling the full cognitive architecture (Filter, Planner).
