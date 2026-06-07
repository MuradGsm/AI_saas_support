from fastapi import FastAPI


app =  FastAPI(
    title="Chat Service",
    version='0.1.0',
)


@app.get('/health')
async def health_chat_service():
    return {"status": "Ok"}