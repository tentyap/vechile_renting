import logging

from django.http import JsonResponse
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

from rest_framework.views import APIView
from rest_framework.authentication import BaseAuthentication,TokenAuthentication
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from rentalsystemapp .serializer import CustomerSerializers
from rentalsystemapp import global_msg
from rentalsystemapp .models import  Customer
from rentalsystemapp .models import  Driver


logger=logging.getLogger('django') 
 
class CustomerCreateAPIView(APIView):
    authentication_classes=[]
    permission_classes=[]
    '''This class create new customer only'''
    def post(self, request):
        if not request.body:
            msg={
                global_msg.RESPONSE_CODE_KEY:global_msg.SUCESS_RESPONSE_CODE,
                global_msg.RESPONSE_MSG_KEY:"sucess"
            }
            return JsonResponse(msg, status = status.HTTP_200_OK)
        try:  
            serializer =CustomerSerializers(data=request.data)
            
            # user=User.objects.get(username='kamal')
            if serializer.is_valid():
                serializer.save()
                # serializer.save(created_by=user)
                msg={
                    global_msg.RESPONSE_CODE_KEY:global_msg.SUCESS_RESPONSE_CODE,
                    global_msg.RESPONSE_MSG_KEY:"SUCESS OF  DATA "
                }
                return JsonResponse(msg, status = status.HTTP_400_BAD_REQUEST)
            msg={
                global_msg.RESPONSE_CODE_KEY:global_msg.UNSUCESS_RESPONSE_CODE,
                global_msg.RESPONSE_MSG_KEY :" invalid  Data in serilize ",
                global_msg.ERROR_KEY:serializer.errors
        }
            return JsonResponse(msg,status=status.HTTP_400_BAD_REQUEST)
        except Exception as exe:
            logger.error(str(exe))
            
            msg={
                global_msg.RESPONSE_CODE_KEY:global_msg.UNSUCESS_RESPONSE_CODE,
                global_msg.RESPONSE_MSG_KEY :"invalid  Data in all"
        }
        return JsonResponse(msg,status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    
class CustomerListApiview(APIView):
    
    authentication_classes=[TokenAuthentication]
    premission_classes=[IsAuthenticated]

    '''This class shows the all the list of student'''
    def get(self,request):
        print(request.headers)
        try: 
            customer=Customer.objects.filter(is_delete=False)#model instance
            print(customer)
            serializers=CustomerSerializers(customer,many=True)#model instance to python
            
            msg={
                    global_msg.RESPONSE_CODE_KEY:global_msg.SUCESS_RESPONSE_CODE,
                    global_msg.RESPONSE_MSG_KEY:"SUCESS OF  DATA ",
                    "data":serializers.data
                }
         
            return JsonResponse(msg, status = status.HTTP_200_OK)
            
        except Exception as exe:
            logger.error(str(exe),exc_info=True)
            msg={
                global_msg.RESPONSE_CODE_KEY:global_msg.UNSUCESS_RESPONSE_CODE,
                global_msg.RESPONSE_MSG_KEY :"invalid  Data"
        }
        return JsonResponse(msg,status=status.HTTP_400_BAD_REQUEST)
    
class CustomerEditApiview(APIView):
    authentication_classes=[TokenAuthentication]
    premission_classes=[IsAuthenticated]
    '''This class updated all the of student'''
    
    def put(self,request,pk):
        print("edit vieww blah blah ")
        if not request.body:
            msg={
                global_msg.RESPONSE_CODE_KEY:global_msg.SUCESS_RESPONSE_CODE,
                global_msg.RESPONSE_MSG_KEY:"sucess"
            }
            return JsonResponse(msg, status = status.HTTP_200_OK)
        try: 
            customer=Customer.objects.get(id=pk, is_delete=False)
            print(customer, "hello manadhar")
            serializer = CustomerSerializers(customer, data=request.data)
            user=User.objects.get(username="kamal")
            if serializer.is_valid():
                serializer.save()
                msg={
                    global_msg.RESPONSE_CODE_KEY:global_msg.SUCESS_RESPONSE_CODE,
                    global_msg.RESPONSE_MSG_KEY:"data update sucessfully "
                }
                return JsonResponse(msg, status = status.HTTP_400_BAD_REQUEST)
            msg={
                global_msg.RESPONSE_CODE_KEY:global_msg.UNSUCESS_RESPONSE_CODE,
                global_msg.RESPONSE_MSG_KEY :"invalid  Data",
                global_msg.ERROR_KEY:serializer.errors
        }
            return JsonResponse(msg,status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist as exe:
            logger.error(str(exe), exc_info=True)
            msg={
                global_msg.RESPONSE_CODE_KEY:global_msg.UNSUCESS_RESPONSE_CODE,
                global_msg.RESPONSE_MSG_KEY :"Not Data Found"
            }   
        except Exception as exe:
            logger.error(str(exe))
            
            msg={
                global_msg.RESPONSE_CODE_KEY:global_msg.UNSUCESS_RESPONSE_CODE,
                global_msg.RESPONSE_MSG_KEY :"invalid  Data"
        }
        return JsonResponse(msg,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    
    
class CustomerDeleteApiview(APIView):
    '''This class delete all the  student'''
    def delete(self,request,pk):
        try:
            student=Customer.objects.get(id=pk)
            student.is_delete = True
            student.save()
            msg={
                    global_msg.RESPONSE_CODE_KEY:global_msg.SUCESS_RESPONSE_CODE,
                    global_msg.RESPONSE_MSG_KEY:"Delete sucessfully "
                }
            return JsonResponse(msg,status=status.HTTP_200_OK)
        except ObjectDoesNotExist as exe:
            logger.error(str(exe), exc_info=True)
            msg={
                global_msg.RESPONSE_CODE_KEY:global_msg.UNSUCESS_RESPONSE_CODE,
                global_msg.RESPONSE_MSG_KEY :"Not Data Found"
            }   
            return JsonResponse(msg,status=status.HTTP_400_BAD_REQUEST)
        except Exception as exe:
            logger.error(str(exe), exc_info=True)
            msg={
                global_msg.RESPONSE_CODE_KEY:global_msg.UNSUCESS_RESPONSE_CODE,
                global_msg.RESPONSE_MSG_KEY :"invalid  Data"
            }
            return JsonResponse(msg,status=status.HTTP_400_BAD_REQUEST)