from pathlib import Path
import os

from langchain_openai import ChatOpenAI, OpenAI
import yaml
openai_key = "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"
def get_current_folder():
    return str(Path(__file__).parent)
def get_llm():
    os.environ["OPENAI_API_KEY"] = openai_key
    llm = ChatOpenAI()
    return llm
def get_prompt(file_name):
    with open(get_current_folder()+f'/prompt_template/{file_name}.yaml',encoding="UTF-8") as f:
        prompt = yaml.safe_load(f)['prompt']
    return prompt

