
from pickle import FALSE
import profile
import re
from django.dispatch import receiver
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from profiles.models import Profile
from django.views import View

from chat.models import Chat, RoomChat
# Create your views here.
def index(request):
    return render(request, 'chat/index.html')
class Index(LoginRequiredMixin, View):
    def get(self, request):
        rooms = RoomChat.objects.filter(Q(sender = request.user.username) | Q(receiver = request.user.username))
        chats = []
        for room in rooms:
            chat = Chat.objects.filter(room = room).last()
            chats.append(chat)
            
        for i in chats:
            print(i.content)
        # rooms = RoomChat.objects.all()
        # chats = Chat.objects.filter(Q(sender = request.user) | Q(receiver = request.user)).order_by['-timestamp']
  
        context = {
            'rooms' : rooms,
            'chats' :chats,
        }
        return render(request, 'chat/chatlist.html',context)

    

class Room(LoginRequiredMixin, View):
    def get(self, request, room_name):
        print("room name:",room_name)

        receiver = room_name
        room_profile = []
        try:
            received_user = User.objects.get(username=room_name)
        except Profile.DoesNotExist:
            received_user = None

        chats = []
       
           
        if RoomChat.objects.filter(sender = request.user.username, receiver = receiver):
                room = RoomChat.objects.filter(sender=request.user.username,receiver=receiver).first()
                chats = Chat.objects.filter(room=room).order_by("timestamp")
                room_name = room.id
                # unread_message = Chat.objects.filter(room=room).last()
                unread_message = Chat.objects.filter(room=room,is_read=False)
                
                for message in unread_message:
                    if message.sender.username != request.user.username:
                        print("chat message 1:",message.content)
                        message.is_read = True
                        message.save()

                
                print("im hereeee")
               
                # return redirect('profiles:thread', pk = threads.pk)
               
        elif RoomChat.objects.filter(sender = receiver,receiver = request.user):
                room = RoomChat.objects.filter(sender = receiver,receiver = request.user.username).first()
                chats = Chat.objects.filter(room=room).order_by("timestamp")
                room_name = room.id
                room_profile = RoomChat.objects.get(id=room.id)
                unread_message = Chat.objects.filter(room=room,is_read=False)
                

                for message in unread_message:
                    if message.sender.username != request.user.username:
                        print("chat message 2:",message.content)
                        message.is_read = True
                        message.save()
                print("im hereeaa")
                # return redirect('profiles:thread', pk = threads.pk)
                # return render(request, 'chat/room.html', {'room_name': room_name, 'chats':chats, 'room':room})
          

        else:
                room = RoomChat(sender=request.user.username,receiver=receiver,sender_profile=request.user, receiver_profile = received_user)
                room.save()
                chat = Chat(sender=request.user, receiver=received_user, room=room)
                chat.save()
                # return render(request, 'chat/room.html', {'room_name': room_name, 'chats':chats, 'room':room})
       
        
        return render(request, 'chat/room.html', {'room_name': room_name, 'chats':chats, 'room':room, 'received_user':received_user})
   

class MessageReadSet(LoginRequiredMixin,View):
    def get(self, request, room_name):
        print("room_name:",room_name)
        receiver = room_name
        if RoomChat.objects.filter(sender = request.user.username, receiver = receiver):
                room = RoomChat.objects.filter(sender=request.user.username,receiver=receiver).first()
                print("room id:",room.id)
                chats = Chat.objects.filter(room=room).last()
                print("chat sender:",chats.sender.username)
                print("request user:",request.user.username)
                if chats.sender.username != request.user.username:
                
                    print("chat message 1:",chats.content)
                    chats.is_read = True
                    chats.save()
                # chats.is_read = True
                # chats.save()
                # room_name = room.id
                
                print("im hereeee")
               
                # return redirect('profiles:thread', pk = threads.pk)
               
        elif RoomChat.objects.filter(sender = receiver,receiver = request.user):
                room = RoomChat.objects.filter(sender = receiver,receiver = request.user.username).first()
                print("room id:",room.id)
                chats = Chat.objects.filter(room=room).last()
                if chats.sender.username != request.user.username:

                    print("chat message 2:",chats.content)
                    chats.is_read = True
                    chats.save()
                # chats.is_read = True
                # chats.save()
                # room_name = room.id
                # chats.is_read = True
                # chats.save()
                # room_profile = RoomChat.objects.get(id=room.id)
                print("im hereeaa")

        return redirect('chat:room',room_name)


def Send_Image(request,room_name):
    if request.method =='POST':
        text_message = request.POST.get("text")
        photo = request.FILES.get("photo")
        sender = User.objects.get(id=request.POST.get("sender"))
        receiver = User.objects.get(username=request.POST.get("receiver"))
        room_id = RoomChat.objects.get(id=request.POST.get("room_id"))
        print("text:",text_message)
        print("photo:",photo)
        print("receiver:",receiver)
        print("sender:",sender)
        print("room:",room_id)
        chat = Chat.objects.create(
            content = text_message,
            sender = sender,
            receiver = receiver,
            photo = photo,
            room = room_id,
            is_read = False,
        )
        chat.save()
        return JsonResponse({"message":"success","current_sender":request.POST.get("sender"),"receiver":request.POST.get("receiver"),"sender_avatar":sender.profile.image.url})
    return JsonResponse({"message":"not"})


def Delete_Message(request,room_name):
    if request.method == 'POST':
        msg_id = request.POST['msg_id']
        print("msg_id:",msg_id)           
        chat = Chat.objects.get(id=msg_id)
        chat.delete()
        print("chat message:",chat.content)
        return JsonResponse({"message":"success","content":chat.content})
    return JsonResponse({"message":"not"})
