from rest_framework import serializers
from api.models import User, inv, bank_details, user_verification, user_details
from django.utils.encoding import force_bytes, force_str, DjangoUnicodeDecodeError, smart_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from account.utils import Util, regex
from django.db import connection
from api.dbquery import getsingledata


class UserRegistrationSerializer(serializers.ModelSerializer):
    # we are writing this becz we need confirm password field in our Registeation
    password2 = serializers.CharField(style={'input_type': 'password'},
                                      write_only=True)
    dob = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)
    address = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)
    city = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)
    pin_code = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)
    mobile = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)

    PAN = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)
    aadhaar_number = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'name', 'password', 'password2', 'tc', 'city',
                  'pin_code', 'PAN', 'aadhaar_number', 'dob', 'address', 'mobile']
        extra_kwargs = {
            'password': {'write_only': True},

        }
        # valdating Password and Confrim Whlie  Registration
        
    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        password2 = attrs.get('password2')
        city = attrs.get('city')
        pin_code = attrs.get('pin_code')
        PAN = attrs.get('PAN')
        aadhaar_number = attrs.get('aadhaar_number')
        dob = attrs.get('dob')
        address = attrs.get('address')
        mobile = attrs.get('mobile')
        print("password", password)
        print("password2", password2)
        res =regex.verificationdoc(PAN,aadhaar_number)
        print("res",res)
        if res ==True:
         if password != password2:
            dict = {'status': 'False'}, {
                'Message': 'Password mismatch'}, {'status': '200'}
            raise serializers.ValidationError(dict)
        else:
         raise serializers.ValidationError("PAN and aadhar formt is wrong")  
        return attrs

    def create(self, validate_data):
        print("******", validate_data)
        print(validate_data['dob'])
        print('select id from api_User where email= %s' %
              validate_data['email'])
        user = User.objects.create_user(**validate_data)
        user_id_insert = "select id from api_User where email= '%s'" % validate_data['email']
        result = getsingledata(user_id_insert)
        #print("user_id_insert id", len(int(result)))
        if result > 0:
            user_details_verification = user_details(
                uid=result, name=validate_data['name'], deleted="N", dob=validate_data['dob'], address=validate_data['address'], city=validate_data['city'],
                mobile=validate_data['mobile'], PAN=validate_data['PAN'], aadhaar_number=validate_data['aadhaar_number'], pin_code=validate_data['pin_code'])
            user_details_verification.save()
            verification_type="PAN"
            if validate_data['PAN'] or validate_data['aadhaar_number']:
             kyc = user_verification(uid=result,deleted="N",verification_type="PAN")
             kyc1 = user_verification(uid=result,deleted="N",verification_type="Kyc_Document")
             kyc.save()
             kyc1.save()
        else:
            raise serializers.ValidationError("Data not insert")
        return user


class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)

    class Meta:
        model = User
        fields = ['email', 'password']


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'name']


class UserChangePasswordVSerializer(serializers.Serializer):
    # print   ('data-------',serializers.password)
    password = serializers.CharField(max_length=255, style={
        'input_type': 'password'
    }, write_only=True)
    password2 = serializers.CharField(max_length=255, style={
        'input_type': 'password'
    }, write_only=True)

    class Meta:
        model = User
        fields = ['password', 'password2']

    def validate(self, attrs):

        password = attrs.get('password')
        password2 = attrs.get('password2')
        user = self.context.get('user')

        if password != password2:
            print("**************", password, password2, user)
            raise serializers.ValidationError(
                "Password and confrim Password does,t match")
        passs = User.objects.filter(email=user).values()[:2]
        print("pass", passs)
        user.set_password(password)
        user.save()
        return attrs


class SendPasswordRestEmailSerilizer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)

    class Meta:
        feilds = ['email']

    def validate(self, attrs):
        email = attrs.get('email')
        if User.objects.filter(email=email):
            user = User.objects.get(email=email)
            # uid =user.id
            uid = urlsafe_base64_encode(force_bytes(user.id))
            print('Encode UID', uid)
            token = PasswordResetTokenGenerator().make_token(user)
            print('Password Rest token', token)
            link = 'http://localhost:3000/api/user/'+uid+'/'+token
            print('Password Rest token', link)
            # send MSg code
            body = 'Click following to rest password'+link

            data = {
                'subject': 'Reset Your Password',
                'body': body,
                'to_email': user.email
            }
            Util.send_email(data)
            return attrs
        else:
            raise serializers.ValidationError('You are not Resigter user')


class UserChangePasswordVSerializer(serializers.Serializer):
    # print   ('data-------',serializers.password)
    password = serializers.CharField(max_length=255, style={
        'input_type': 'password'}, write_only=True)
    password2 = serializers.CharField(max_length=255, style={
        'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['password', 'password2']

    def validate(self, attrs):

        try:
            password = attrs.get('password')
            password2 = attrs.get('password2')
            uid = self.context.get('uid')
            token = self.context.get('token')
            print("Rest passwordpassword", password, "password2",
                  password2, "uid", uid, "token", token)
            if password != password2:
                print("**************", password, password2, uid)
                raise serializers.ValidationError(
                    "Password and confrim Password does,t match")
            id = smart_str(urlsafe_base64_decode(uid))
            print("base64 decode id or user uid", id)
            user = User.objects.get(id=id)
            print("query with id user", user)
            if not PasswordResetTokenGenerator().check_token(user, token):
                raise serializers.ValidationError(
                    "Token is not Valid or Expired")

            user.set_password(password)
            user.save()
            return attrs
        except DjangoUnicodeDecodeError as identifier:
            PasswordResetTokenGenerator().check_token(user, token)


class AddBankDetialsSerializer(serializers.ModelSerializer):
    uid = serializers.CharField(max_length=255, style={
        'input_type': 'uid'
    }, write_only=True)

    class Meta:
        model = bank_details

        fields = ['account_holder', 'bank_name', 'ifsc_code',
                  'account_number', 'uid', 'branch_address']

    def validate(self, attrs):

        uid = attrs.get('uid')
        account_holder = attrs.get('account_holder')
        bank_name = attrs.get('bank_name')
        ifsc_code = attrs.get('ifsc_code')
        branch_address = attrs.get('branch_address')
        account_number = attrs.get('account_number')
        re = regex.isaccountvaildation(account_number)
        regex1 = regex.isValidIFSCCode(ifsc_code)
        print("Re", re, "ifsc", regex1)

        uid1 = inv.objects.filter(uid_id=uid).values()
        print("ttt", len(uid1))
        if re == False:
            raise serializers.ValidationError("Account number is validation")

        else:
            if regex1 == False:
                raise serializers.ValidationError("ifsc code is validation")
            else:
                if len(uid1) == 0:
                    raise serializers.ValidationError("Uid not found")
                else:
                    uid1 = bank_details.objects.filter(uid=uid).values('uid')
                    print("uid1", uid1)
                    for uid in uid1:
                        if uid == uid:
                            print("uid already exist", uid)
                            raise serializers.ValidationError(
                                "Uid already exits")
                    else:
                        print("hhellllllll")
                        query = bank_details(account_holder=account_holder, deleted="N", bank_name=bank_name,
                                             ifsc_code=ifsc_code, account_number=account_number, branch_address=branch_address, uid=uid)
                        query.save()
                        bank_uid = 'select uid from api_bank_details where uid= %s' % uid
                        bank_uid = getsingledata(bank_uid)
                        print("uid88988", uid, bank_uid)
                        if bank_uid == int(uid):
                            print("gggggggggggggggggg")
                            query = user_verification(
                                uid=bank_uid, verification_type="Account_details", deleted="N")

                            query.save()
                        else:
                            raise serializers.ValidationError(
                                "data not insert in bank details")

        return attrs
