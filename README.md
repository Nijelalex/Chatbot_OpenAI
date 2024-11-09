# Chatbot OpenAI

This Chatbot allows a document to be uploaded and then user can ask questions to get responses.

**Architecture**

1. The Application uses streamlit for UI through which user interaction like uploading of document (PDF) and entering question is performed.
2. Langchain framework is used for text extraction and breaking into text chunks. OpenAPI is used to generate embeddings
3. FAISS is used for Vector store of embeddings and performing similarity search of user question. 
4. The LLM model used is Open AI "gpt-3.5-turbo" which generates the response for the question. 

