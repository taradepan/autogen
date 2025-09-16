# Multi-Agent Conversational AI with pyautogen

This project demonstrates the use of the `pyautogen` library to create multi-agent conversational applications. It includes two distinct scenarios: a simple two-agent interaction and a more complex group chat for research tasks. The project relies on OpenAI's GPT models for language understanding and generation.

## Features

- **Two-Agent Setup (`main.py`)**: A basic example of a conversation between an `AssistantAgent` (CTO) and a `UserProxyAgent` to perform simple coding tasks.
- **Multi-Agent Group Chat (`research.py`)**: A more advanced scenario with a group of agents (Admin, Engineer, Scientist, Planner, Critic) collaborating on a research task.
- **Dynamic Code Execution**: Agents can write and execute Python code to solve tasks, with the output saved to designated directories.
- **LLM Configuration**: Easy configuration of the language model using a `.env` file for API keys.

## Getting Started

Follow these instructions to set up and run the project on your local machine.

### Prerequisites

- Python 3.8 or higher
- An OpenAI API key

### Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

### Configuration

1. **Create a `.env` file** in the root directory of the project by copying the example file:
   ```bash
   cp .env.example .env
   ```

2. **Add your OpenAI API key** to the `.env` file:
   ```
   OPENAI_API_KEY="your-api-key"
   ```

## Usage

You can run the two different scenarios as follows:

*   **To run the simple two-agent setup:**
    ```bash
    python main.py
    ```
    The output and generated code will be saved in the `web/` directory.

*   **To run the multi-agent research task:**
    ```bash
    python research.py
    ```
    The output and generated code will be saved in the `code/` directory.

## Project Structure

*   **`main.py`**: Implements a basic two-agent setup where a "CTO" agent assists a user proxy with simple coding tasks.
*   **`research.py`**: Showcases a multi-agent group chat for a research task, involving planning, coding, and verification.
*   **`requirements.txt`**: Lists the necessary Python packages for the project (`pyautogen`, `openai`, `python-dotenv`).
*   **`.gitignore`**: Specifies files and directories to be ignored by Git, such as the `.env` file, cache, and output directories (`/code`, `/web`).

## Agent Roles

### In `main.py`

*   **CTO (`AssistantAgent`)**: The primary agent responsible for generating code and providing solutions to the user's requests.
*   **user_proxy (`UserProxyAgent`)**: Represents the user, initiates the conversation, and can execute the code provided by the CTO.

### In `research.py`

This script uses a group chat managed by a `GroupChatManager`. The agents collaborate to achieve a common goal.

*   **Admin (`UserProxyAgent`)**: Represents the user and acts as the final approver for the proposed plan. The plan execution will not start without the Admin's approval.
*   **Planner (`AssistantAgent`)**: Responsible for creating a step-by-step plan to address the user's request. The plan is revised based on feedback from the Admin and the Critic.
*   **Engineer (`AssistantAgent`)**: Executes the approved plan by writing and saving the necessary code.
*   **Scientist (`AssistantAgent`)**: Analyzes and categorizes information, such as research papers, based on their abstracts. This agent does not write code.
*   **Critic (`AssistantAgent`)**: Reviews the plan, code, and claims made by other agents to ensure accuracy and completeness. It provides feedback for improvement.

## How it Works

The `pyautogen` library allows for the creation of a network of agents that can communicate with each other to solve complex tasks. Each agent is configured with a specific role and capabilities, defined by its system message and configuration.

In `main.py`, the `user_proxy` initiates a chat with the `CTO` agent, which then generates Python code to fulfill the request. The `user_proxy` executes the code in the `web` directory.

In `research.py`, the `user_proxy` (Admin) initiates a chat with the `GroupChatManager`. The Planner suggests a plan, which is then reviewed by the Critic and approved by the Admin. The Engineer and Scientist then execute the plan, with the Critic providing feedback throughout the process. The final output is saved in the `code` directory.

---

This documentation provides a comprehensive overview of the project. For more details on the `pyautogen` library, please refer to the [official documentation](https://microsoft.github.io/autogen/).


