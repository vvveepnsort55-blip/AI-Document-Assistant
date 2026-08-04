import os
import requests



class AIService:


    def __init__(self):

        self.api_key = os.getenv(
            "AI_API_KEY"
        )


        self.model = os.getenv(
            "AI_MODEL",
            "openrouter/free"
        )


        self.url = (
            "https://openrouter.ai/api/v1/chat/completions"
        )



    def ask(
        self,
        question: str,
        context: str,
        history: list = None
    ):


        if not self.api_key:

            return (
                "AI API key is missing."
            )



        headers = {

            "Authorization":
            f"Bearer {self.api_key}",

            "Content-Type":
            "application/json",

            "HTTP-Referer":
            "http://localhost:8000",

            "X-Title":
            "AI Document Assistant"

        }



        messages = []


        # System instruction

        messages.append({

            "role": "system",

            "content":
            """
You are an AI document assistant.

Rules:
- Answer only using the provided document context.
- Do not use outside knowledge.
- Use conversation history only to understand references.
- If the answer is not available in the document, say:
"I could not find this information in the document."
- Keep answers clear and concise.
"""

        })



        # Conversation memory

        if history:


            for item in history[-5:]:


                messages.append({

                    "role": "user",

                    "content":
                    item["question"]

                })


                messages.append({

                    "role": "assistant",

                    "content":
                    item["answer"]

                })



        # Current question + RAG context

        messages.append({

            "role": "user",

            "content":
            f"""

Document Context:

{context}


Current Question:

{question}

"""

        })



        data = {

            "model":
            self.model,


            "messages":
            messages,


            "temperature":
            0.2

        }



        try:


            response = requests.post(

                self.url,

                headers=headers,

                json=data,

                timeout=60

            )



            result = response.json()



            if "choices" not in result:


                print(

                    "OpenRouter Error:",

                    result

                )


                return (
                    "Unable to generate answer."
                )



            return (

                result["choices"][0]

                ["message"]

                ["content"]

            )



        except Exception as e:


            print(

                "AI Error:",

                e

            )


            return (
                "AI service unavailable."
            )
