from fastapi import FastAPI, Request

from chains import get_conversational_rag_chain
from evolution_api import send_whatsapp_message
from vectorstore import load_documents

from config import AUTORIZED_CHATS

app = FastAPI()

conversational_rag_chain = get_conversational_rag_chain()

@app.post('/webhook')
async def webhook(request: Request):
    data = await request.json()
    chat_id = data.get('data').get('key').get('remoteJid')
    message = data.get('data').get('message').get('conversation')

    if chat_id and chat_id not in AUTORIZED_CHATS:
        return {'status': 'ok'}

    if message and 'dadbot:' not in message.lower():
        return {'status': 'ok'}
    message = message[8:]

    if chat_id and message:
        if message == 'update_data' and chat_id == '5511974282313@s.whatsapp.net':
            load_documents()
            send_whatsapp_message(
                number=chat_id,
                text="Documentos inseridos com sucesso!",
            )
            return {'status': 'ok'}

        ai_response = conversational_rag_chain.invoke(
            input={'input': message[8:]},
            config={'configurable': {'session_id': chat_id}},
        )['answer']

        text_response = message[::-1] + '\n\n*DadBOT Explica:*  ' + ai_response

        send_whatsapp_message(
            number=chat_id,
            text=text_response,
        )

    return {'status': 'ok'}
