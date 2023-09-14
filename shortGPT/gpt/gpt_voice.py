
from shortGPT.gpt import gpt_utils
def getGenderFromText(text):
    chat, system = gpt_utils.load_local_yaml_prompt('prompt_templates/voice_identify_gender.yaml')
    chat = chat.replace("<<STORY>>", text)
    result = gpt_utils.gpt3Turbo_completion(chat_prompt=chat, system=system).replace("\n", "").lower()
    return 'female' if 'female' in result else 'male'