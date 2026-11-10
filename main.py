from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langsmith import traceable

import os
load_dotenv()

@traceable(name="hello-world", run_type="llm")
def main():
    print("Hello from langchain-course!")
    ##print("Your GOOGLE_API_KEY is:", os.getenv("GOOGLE_API_KEY"))
    llm = ChatGoogleGenerativeAI(model="gemini-3.5-flash", temperature=0.0)

    prompt = PromptTemplate(
                    input_variables=["topic"],
                    template="Write a poem about {topic}.",
                )
    
    response = llm.invoke(
            prompt.format(topic="LangChain")
    )

    print(response.content[0]["text"])

if __name__ == "__main__":
    main()
