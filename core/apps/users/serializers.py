from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from dj_rest_auth.registration.serializers import RegisterSerializer
from django.contrib.auth import get_user_model
from rest_framework import serializers
import logging


logger = logging.getLogger(__name__)


User = get_user_model()

# {✪} UserSerializer - Output Serializer 
class UserSerializer(serializers.ModelSerializer): 
    profile_photo = serializers.ReadOnlyField(source="profile.profile_photo.url")

    # WARN no role ?
    # WARN profile_photo ?
    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "first_name",
            "last_name",
            "profile_photo",
        ]

    def to_representation(self, instance):
        representation = super(UserSerializer, self).to_representation(instance)
        if instance.is_superuser:
            representation["admin"] = True
        return representation
    
# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# {✪} CustomRegisterSerializer - Input Serializer
class CustomRegisterSerializer(RegisterSerializer):  
    
    # _PIN_ this is the register serializer used by the dj-rest-auth  

    """ 
    NOTE 
        Users created by this serializer won't have the create_user method from the CustomUserManager invoked. 
        Users created with the CustomUserManager won't response with a jwt token. 
    """

    username = None
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    role = serializers.CharField(required=False)
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)


    def validate_role(self, value):
        valid_choices = [choice[0] for choice in User.ROLES]
        if value not in valid_choices:
            return 'user'  
        return value


    def get_cleaned_data(self):
        super().get_cleaned_data()
        return {
            "email": self.validated_data.get("email", ""),
            "first_name": self.validated_data.get("first_name", ""),
            "last_name": self.validated_data.get("last_name", ""),
            "password1": self.validated_data.get("password1", ""),
            "role": self.validated_data.get("role", ""),
        }
    

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        
        logger.info("● save() called ") # _LOG_ ● save ↯ 

        setup_user_email(request, user, [])
        user.email = self.cleaned_data.get("email")
        user.password = self.cleaned_data.get("password1")
        user.first_name = self.cleaned_data.get("first_name")
        user.last_name = self.cleaned_data.get("last_name")
    
        # _PIN_ Custom role handle 

        _role = self.cleaned_data.get("role")
        user.role = self.validate_role(_role)

        if user.role == 'super':
            user.is_staff = True
            user.is_superuser = True

        elif user.role == 'admin' or user.role == 'staff':
            user.is_staff = True
            user.is_superuser = False

        else:
            user.is_staff = False
            user.is_superuser = False

        user = adapter.save_user(request, user, self)
        user.save()

        return user
    
# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .



    