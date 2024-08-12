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

