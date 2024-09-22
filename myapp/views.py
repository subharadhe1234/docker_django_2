from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from firebase_admin import firestore,db,storage
from django.views.decorators.csrf import csrf_exempt
import jwt
from datetime import datetime
from django.contrib.auth.models import User,Group
from rest_framework import routers, serializers, viewsets,generics,status
from .serializers import UserSerializer
from .models import ExampleModel 
from rest_framework.response import Response
# Firebase Firestore client initialization
firestore_client = firestore.client()
from rest_framework.views import APIView
# doc_ref = firestore.collection("users")

# realtime database initialization



# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
# from rest_framework.decorators import permission_classes
# from rest_framework.permissions import AllowAny

# # from rest_framework.renderers import JSONRenderer
# # import io
# from rest_framework.parsers import JSONParser



# class Comment:
#     def __init__(self,email,content,created=None) :
#         self.email = email
#         self.content = content
#         self.created = created or datetime.now()






# @api_view(['GET','POST','PUT','DELETE'])
# @permission_classes([AllowAny])  # Optional: Add permission class if needed
# def admin(request):  # Corrected parameter name


# # .=====================GET=================
#     if request.method=='GET':
#         data = {
#             'name': 'radhe',
#             'age': ['14', '45', '78', '10'],
#             'pos': 'krishna'
#         }
        
#         comment =Comment(email="Radhe@gmail.com",content="hare krishna")
#         serializers=CommentSelizer(comment)
#         data =serializers.data

#         json = JSONRenderer().render(data)
#         stream = io.BytesIO(json)
#         parse = JSONParser().parse(stream)
#         srl=CommentSelizer(data=parse)
#         srl.is_valid()
#         val_data=srl.validated_data
#         # cret_data=serializers.create(validated_data=val_data)
#         # print(cret_data)

#         print(val_data)
#         return Response(parse)
    
# # .=====================POST=================
#     elif request.method == 'POST':
#         data=request.data
#         return Response({'result':'this is the POST requrest'})
    

# # .=====================PUT=================
#     elif request.method == 'PUT':
#         return Response({'result':'this is the PUT requrest'})
    

# # .=====================DELET=================
#     elif request.method == 'DELETE':
#         return Response({'result':'this is the DELETE requrest'})












# Simple index view
def index(request):
    return HttpResponse("radhe")



@csrf_exempt  # Disable CSRF for this endpoint
def data_request(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        # doc_ref.document("krishna").set(data)  # Store data in Firestore under "krishna"
        # print(data)
        # users_ref = firestore_client.collection("users")
        # docs = users_ref.stream()
        # print(docs)
        # for doc in docs:
            # print(f"{doc.id} => {doc.to_dict()}")
        # realtime_db=db.reference("radhe").child("scores")
        # snapshot = realtime_db.order_by_value().get()   
        # for key, val in snapshot.items():
        #     print('The {0} dinosaur\'s score is {1}'.format(key, val))
        # print(snapshot)
        # print(request.GET)
        return JsonResponse({'result': data})
    
@csrf_exempt
def encription(requrest):
    if requrest.method == 'POST':
        data = json.loads(requrest.body.decode('utf-8'))
        secte_key="LKzLPry74GkbHoN_yBGon68lw2zdwexy6S7jcWjjPBoK16aoiNcpMTecoCPR1y9c "
        paylode={
            'user_id':'abc123',
            'username':"subhadip",
            'role':'user'
        }
        # tocken=jwt.encode(paylode,secte_key,algorithm='HS256')
        # print(tocken)
        tocken='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiYWJjMTIzIiwidXNlcm5hbWUiOiJzdWJoYWRpcCIsInJvbGUiOiJ1c2VyIn0.hLZ5xmuZL0AmVYoAhqEwYsOLyEbnkp2m0vKaFUZSnxM'
        decode_paylode=jwt.decode(tocken,secte_key,algorithms=['HS256'])
        print(decode_paylode)
        # eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiYWJjMTIzIiwidXNlcm5hbWUiOiJzdWJoYWRpcCIsInJvbGUiOiJhZG1pbiJ9.HiV5_F1sOHJyILRPicOcMEd29HjieLgpgeRw8iqKmww
        # eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiYWJjMTIzIiwidXNlcm5hbWUiOiJzdWJoYWRpcCIsInJvbGUiOiJ1c2VyIn0.hLZ5xmuZL0AmVYoAhqEwYsOLyEbnkp2m0vKaFUZSnxM
        return JsonResponse({'result': data})
    


class UserViewSet(generics.ListCreateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = ExampleModel.objects.all()
    serializer_class = UserSerializer
    # lookup_field = "pk"
    # permission_classes = [permissions.IsAuthenticated]


# class GroupViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Group.objects.all().order_by('name')
#     serializer_class = GroupSerializer
#     lookup_field = "pk"
    # permission_classes = [permissions.IsAuthenticated]





