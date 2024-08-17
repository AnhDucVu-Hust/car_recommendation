from pathlib import Path
import os

from langchain_openai import ChatOpenAI, OpenAI
import yaml
openai_key = "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"
def get_current_folder():
    return str(Path(__file__).parent)
def get_llm():
    os.environ["OPENAI_API_KEY"] = openai_key
    llm = ChatOpenAI(model="gpt-4o-mini",temperature=0)
    return llm
def get_prompt(file_name):
    with open(get_current_folder()+f'/prompt_template/{file_name}.yaml',encoding="UTF-8") as f:
        prompt = yaml.safe_load(f)['prompt']
    return prompt

