from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import status
from api.models import User, inv, bank_details
from api.serializer import UserRegistrationSerializer, UserLoginSerializer, UserProfileSerializer, UserChangePasswordVSerializer, SendPasswordRestEmailSerilizer, AddBankDetialsSerializer, UserChangePasswordVSerializer, ImageSerializer, planserilizers, Transcatin_intiatie_serializers
from django.contrib.auth import authenticate
from account.renderers import UserRenderer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from django.core.mail import EmailMessage, send_mail
from rest_framework.parsers import MultiPartParser
from account.utils import imageconvert
from api.dbquery import getsingledata, getselectdata
from account.database import selectdata, insertQuery, getGenralQueryData
import json
import datetime
from api.getverifcation import verification


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class UserRegistrationView(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request, format=None):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            id = User.objects.filter(email=user).values_list('id', flat=True)
            print("id*****", id)
            for x in id:
                print("8880", x)
                print(type(x))
                inv_state = 0
                deleted = 'N'
                Inv = inv(uid_id=x, inv_state=inv_state, deleted=deleted)
                Inv.save()
                id1 = inv.objects.filter(uid=x).values()
                print("id1****", id1)
            token = get_tokens_for_user(user)

            return Response({'status': 'True', 'Message': 'Registration success', 'status': '200', 'result': serializer.data, 'token': token}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_CREATED)


class UserLoginView(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                token = get_tokens_for_user(user)

                return Response({'msg': 'Login Success', 'token': token}, status=status.HTTP_200_OK)
            else:
                return Response({'errors': {'non_field_error': ['Email or Password is not Valid']}},
                                status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)


class UserProfileView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        serlializer = UserProfileSerializer(request.user)
        return Response(serlializer.data, status=status.HTTP_200_OK)


class UserChangePasswordView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):

        serilizer = UserChangePasswordVSerializer(
            data=request.data, context={'user': request.user})
        # serilizer =UserChangePasswordVSerializer(password=password['password'], password2=password['password2'])
        # print('serilizer---',serilizer)

        if serilizer.is_valid(raise_exception=True):
            print("serilise=======>", serilizer.data)
            return Response({'msg': 'Password Changed succesfully'}, status=status.HTTP_200_OK)

        return Response(serilizer.errors, status=status.HTTP_404_BAD_REQUEST)


class SendPasswordRestEmailView(APIView):
    renderer_classess = [UserRenderer]

    def post(self, request, fromat=None):
        serializer = SendPasswordRestEmailSerilizer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            return Response({'msg': 'Passwordrest link send on email'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)


class UserPasswordRestView(APIView):
    renderer_classess = [UserRenderer]

    def post(self, request, uid, token, fromat=None):
        serializer = UserChangePasswordVSerializer(
            data=request.data, context={'token': token, 'uid': uid})
        if serializer.is_valid(raise_exception=True):
            return Response({'msg': 'Password change sucessful'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)


class Sendmail(APIView):
    def get(self, request, fromat=None):
        send_mail('Testing Mail',
                  'Here is the message',
                  'golusingh19479@gmail.com',
                  ['tej.pratap@faircent.com'], fail_silently=False, )

        return Response({'mg:sussecs'})


class AddBankDetials(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request, Format=None):
        serializer = AddBankDetialsSerializer(data=request.data)
        print("request data of bank", request.data)
        if serializer.is_valid(raise_exception=True):
            return Response({'msg': 'Add Bank succefully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)


class Imageupload(APIView):
    parser_classes = (MultiPartParser,)

    def post(self, request, *args, **kwargs):
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            image = serializer.validated_data['image']
            # Save the image to your server or process it as required
            return Response({'status': 'success'})
        else:
            return Response(serializer.errors, status=400)


class planview(generics.ListCreateAPIView):
    def get(self, request, inv_id):

        plan = []
        content = {}
        serializer = planserilizers(
            data=request.data, context={'inv_id': inv_id})

        if serializer.is_valid(raise_exception=True):
            data = serializer.context.get('inv_id')
            print("daatatta", data)
            try:
                invs = selectdata(
                    'select inv_state from api_inv where id= %s' % data)
                print("ddddddddddddddddddddddd", len(invs))
                if invs.inv_state[0] == 10000:
                    queryresult = selectdata(
                        'select cnd_name ,rate,min_proposal,cnd_parent_id,description from api_cnd where cnd_group="SIGP_PLAN_NAME"')
                    print("****************************", queryresult)
                    queryresult = queryresult.rename(columns={'cnd_name': 'plan_name', 'rate': 'plan_rate', 'min_proposal': 'mini_invtesment', 'cnd_parent_id': 'plan_id',
                                                              'description': 'plan_descripation'})
                    data = queryresult.to_dict(orient='records')

                    print(data)

                    return Response({"msg": "user made live please check kyc is complete or not", "data": data, "status": True})
                elif len(invs) == 0:
                    return Response({"data": "Lender doe not exits", "status": False})
                else:
                    return Response({"data": "User is not live Please contact support team", "status": False})
            except:

                return Response({"data": "data not found", "status": False})

        else:
            return Response(serializer.errors, status=400)


class Transcatin_intiatie(APIView):
    def post(self, request, format=None):
        serializer = Transcatin_intiatie_serializers(data=request.data)
        if serializer.is_valid(raise_exception=True):
            data = serializer.validated_data
            bank_ref_id = data["bank_ref_id"]
            plan_id = data["plan_id"]
            amount = data["amount"]
            investment_id = data["inv_id"]
            pt_ref_id = data["pt_ref_id"]
            txn_date = str(data["txn_date"])
            pg_type = data['pg_type']
            payment_mode = data['payment_mode']
            '''pg_type_str=f"'{pg_type}'"
                bank_ref_id_str=f"'{bank_ref_id}'"
                payment_mode_str=f"'{payment_mode}'"
                '''
            txn_status = 500
            pool_id = 43
            pool_loan_id = 1003810388
            created = datetime.datetime.now()
            res = verification.getverication(investment_id)
            tables = "api_b2b_product_investment_utr_detail"
            print("pt_ref_id**************", type(pt_ref_id))
            print("bank_ref_id******************", type(bank_ref_id))
            # print("response of kyc function return",len(res['pending_document']))
            if res['status'] == True and len(res['pending_document']) == 0:
                query = f'select bank_ref_id,txn_id from {tables} where bank_ref_id="{bank_ref_id}" or txn_id={pt_ref_id} and deleted="N"'
                check_for_bank_ref_id = getGenralQueryData(query)
                print(check_for_bank_ref_id)
                print(query)

                # existdata=check_for_bank_ref_id[0][0]
                # existdata1=check_for_bank_ref_id[0][1]
                # print("existdata*******************",existdata)
                if len(check_for_bank_ref_id) == 0:
                    vaule = (bank_ref_id, pg_type, payment_mode, pt_ref_id, investment_id, amount, plan_id,
                             txn_date, created.strftime('%Y-%m-%d %H:%M:%S'), txn_status, pool_id, pool_loan_id)
                    field = "(bank_ref_id, pg_type, payment_mode,txn_id,investment_id,amount,plan_id,txn_date,created,txn_status,pool_id,pool_loan_id)"
                    insert_id = insertQuery(tables, field, vaule)
                    data = {"message": "Transaction Executed Successfully", "success": True, "result": {
                        "fc_txn_id": insert_id, "txn_status": "INITIATED", "amount": amount}}
                    return Response(data)

                else:
                    return Response({"data": {"data already exists"}})

            elif res['status'] == True and len(res['pending_document']) > 0:
                return Response({"data": res})
            else:
                return Response({"data": res})

        else:
            return Response(serializer.errors, status=400)

            # existdata==bank_ref_id and existdata1==int(pt_ref_id)
