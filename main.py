from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import openai
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


print("PDF LOADER ===================>>>>>>>>>>>>>> ")

from langchain.document_loaders import PyPDFLoader

loader=PyPDFLoader("./Hands_On.pdf")
pages = loader.load()
page = pages[0]

print("___________ Page first", page)

print("___________ Page first content", page.page_content[:5])

print("___________ Document len", len(pages))

print("END PDF LOADER ===================>>>>>>>>>>>>>> ")

























app = FastAPI()





class DocumentRequest(BaseModel):
    content: str
    model: Optional[str] = "gpt-3.5-turbo"

class DocumentResponse(BaseModel):
    processed_content: str


@app.get("/")
async def read_root():
    return { "Message": "Welcome to Document Loading API" }

# @app.get("/load-document")
# async def load_docs():
#     pages = loader.load()
#     page = pages[0]

#     print("Page Metadata: ",page.metadata)

#     return {
#         len: len(pages),
#     }




# # Add this at the bottom if you want to run directly
# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)