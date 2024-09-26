from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from dj_rest_auth.registration.serializers import RegisterSerializer
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from rest_framework import serializers
import logging



from apps.profiles.models import Profile

logger = logging.getLogger(__name__)


User = get_user_model()

# {✪} UserSerializer - Output Serializer 
class UserSerializer(serializers.ModelSerializer): 

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "first_name",
            "last_name",
            "user_group",
        ]

    def to_representation(self, instance):
        representation = super(UserSerializer, self).to_representation(instance)
        if instance.is_superuser:
            representation["admin"] = True
        return representation
    
# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .



# {✪} AUthGroupSerializer 
class AUthGroupSerializer(serializers.ModelSerializer): 

    class Meta:
        model = Group
        fields = [
            "id",
            "name",
        ]




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
    user_group = serializers.IntegerField(required=False)
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)



    def validate_group(self, value):
        choices = [group['id'] for group in Group.objects.values()]
        if value not in choices:
            return Group.objects.get(id = 4)
        return Group.objects.get(id = value)


    def get_cleaned_data(self):
        super().get_cleaned_data()
        return {
            "email": self.validated_data.get("email", ""),
            "first_name": self.validated_data.get("first_name", ""),
            "last_name": self.validated_data.get("last_name", ""),
            "password1": self.validated_data.get("password1", ""),
            "user_group": self.validated_data.get("user_group", ""),
        }
    

    def save(self, request):

        logger.info("● save() called ") # [LOG] ● save ↯ 
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        
    
        user.email = self.cleaned_data.get("email")
        user.password = self.cleaned_data.get("password1")
        user.first_name = self.cleaned_data.get("first_name")
        user.last_name = self.cleaned_data.get("last_name")
        # user.user_group = self.cleaned_data.get("user_group")  

        # _PIN_ Handling group role 
        _group = self.cleaned_data.get("user_group")  
        user.user_group = self.validate_group(_group)

        if user.user_group == 'super':
            user.is_staff = True
            user.is_superuser = True

        elif user.user_group == 'admin' or user.user_group == 'staff':
            user.is_staff = True
            user.is_superuser = False

        else:
            user.is_staff = False
            user.is_superuser = False

        user = adapter.save_user(request, user, self)
        user.save()

        setup_user_email(request, user, [])

        return user
    
# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
    

    
