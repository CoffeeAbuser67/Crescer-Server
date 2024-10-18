from rest_framework import serializers
from .models import Patient
from datetime import date



# {✪} PatientBriefSerializer
class PatientBriefSerializer(serializers.ModelSerializer):
    
    today = date.today() 

    age = serializers.SerializerMethodField()
    isValid = serializers.SerializerMethodField()

    class Meta:
        model = Patient
        fields = ['pkid', 'patient_name', 'age', 'isValid' ]  # Only include a few fields


    def get_age(self, obj):
        
        age = self.today.year - obj.birth_date.year - ((self.today.month, self.today.day) < (obj.birth_date.month, obj.birth_date.day))
        return age

    def get_isValid(self, obj):
        isValid = self.today <= obj.expiration_date
        return isValid


# {✪} PatientSerializer
class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = [
            'pkid', 
            'patient_name', 
            'parent_name', 
            'phone_number', 
            'email', 
            'note', 
            'birth_date', 
            'expiration_date',
            'created_at', 
        ]
        read_only_fields = ['created_at', 'updated_at']


# {✪} PatientNoteSerializer
class PatientNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['note']  