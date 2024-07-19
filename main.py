import os
import autogen
import dotenv
dotenv.load_dotenv()


config_list = [
    {
        'model': 'gpt-4o-mini',
        'api_key': os.getenv("OPENAI_API_KEY")
    }
]

llm_config={
    "seed": 42,
    "config_list": config_list,
    "temperature": 0
}

assistant = autogen.AssistantAgent(
    name="CTO",
    llm_config=llm_config,
    system_message="Chief technical officer of a tech company"
)

user_proxy = autogen.UserProxyAgent(
    name="user_proxy",
    human_input_mode="NEVER",
    max_consecutive_auto_reply=10,
    is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
    code_execution_config={"work_dir": "web", "use_docker": False},
    llm_config=llm_config,
    system_message="""Reply TERMINATE if the task has been solved at full satisfaction.
Otherwise, reply CONTINUE, or the reason why the task is not solved yet."""
)

task = """
Write python code to output numbers 1 to 100, and then store the code in a file.
"""

user_proxy.initiate_chat(
    assistant,
    message=task
)

task2 = """
write a python code to show demo for recursion and store it in a file. 
"""

user_proxy.initiate_chat(
    assistant,
    message=task2
)
