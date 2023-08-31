import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.generic.websocket import JsonWebsocketConsumer
from .models import Chat

# class ChatConsumer(JsonWebsocketConsumer):
#     def connect(self):
#         print("ChatConsumer::connect: " + str(self.scope["user"]))

#         self.accept()

#         self.room_id = None
    
#     def receive_json(self, content):

#         print("ChatConsumer::receive_json")

#         command = content.get("command", None) 
#         try:
#             if command == "join":
#                 print("joing room: " + str(content["room"]))
#                 self.join_room(content["room"])
#             elif command == "send":
#                 print("sending message: " + str(content["message"] ))
#                 self.send_room(content["room"], content["message"] )
#             elif command == "leave":
#                 self.leave_room(content["room"])
#             else: 
#                 pass
#         except ClientError as e: 
#             self.handle_client_error(e)





class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, code):
        pass

    async def receive(self, text_data=None, bytes_data=None):
        if text_data:
            data = json.loads(text_data)
            message = Chat.objects.create(text)
            await self.send(text_data=json.dumps({"message": data['message']}))
        elif bytes_data:
            await self.send(bytes_data=bytes_data)
