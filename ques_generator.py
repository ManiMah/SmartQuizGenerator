import requests
import json
API_TOKEN = 'hidden'  


API_URL = "https://router.huggingface.co/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {API_TOKEN}",
}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    if response.status_code != 200:
        raise Exception(f"Request failed: {response.status_code}, {response.text}")
    
    return response.json()

def ques_generator(text, num_ques):
    payload = {
        "messages": [
            {
                "role": "user",
                "content": (
                    f"Generate {num_ques} quiz questions for the given text in english only: \n\n{text}\n\n"
                    "Return only JSON format as below:\n"
                    "{\n"
                    "  \"question\": \"[Your Quiz Question]\",\n"
                    "  \"answer\": \"[Correct Answer]\",\n"
                    "  \"distractors\": [\"[Distractor 1]\", \"[Distractor 2]\", \"[Distractor 3]\"],\n"
                    "   \"Reason\":\"[reason for correct answer ]\",\n"
                    "  \"difficulty\": \"[Difficulty Level]\",  // e.g., easy, medium, hard\n"
                    "  \"topic\": \"[Related Topic]\"\n"
                    "}")
            }
        ],
        "model": "openai/gpt-oss-120b:groq"
    }

    response = query(payload)
    print("Response:", response)



    try:
        generated_text = response["choices"][0]["message"]["content"].strip()
        questions = json.loads(generated_text)
        return questions
    except (IndexError, KeyError, json.JSONDecodeError) as e:
        raise Exception(f"Error in parsing the generated text. The error is due to {e}")


























    """questions = []
    try:
        question_data = {
            "question": generated_text.split("Question: ")[1].split("Answer: ")[0].strip(),
            "answer": generated_text.split("Answer: ")[1].split("Distractors: ")[0].strip(),
            "distractors": generated_text.split("Distractors: ")[1].split("Difficulty: ")[0].strip().split(", "),
            "difficulty": generated_text.split("Difficulty: ")[1].split("Topic: ")[0].strip(),
            "topic": generated_text.split("Topic: ")[1].strip()
        }
        questions.append(question_data)
    except (IndexError, ValueError) as e:
        raise Exception(f"Error in parsing the generated text.The error is due to {e}")

    return questions"""



#testing o/p
"""try:
    text_input = "The Indian independence movement was a series of political efforts from the middle of the nineteenth century to 1947, that took place in the Indian subcontinent with the aim of ending British colonial rule.The first half of the 20th century saw a progressively radical approach towards self-rule. From the protests against the Partition of Bengal (1906) that exposed the limits of the reformist agenda of the moderate leaders to the Non cooperation movement (1919-1922) that saw demands for not cooperating with the colonial authorities through the Civil Disobedience Movement (1929-1931) that called for active disobedience to the colonial government to the Quit India Movement (1942) that categorically demanded the end of British colonial presence in India, the independence movement gathered momentum steadily and ultimately resulted in the transfer of power in 1947.[1] "
    ao = ques_generator(text_input,2)
    print(ao)
except Exception as e:
    print(f"An error occurred: {e}")"""
