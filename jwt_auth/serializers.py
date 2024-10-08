from rest_framework import serializers
from django.contrib.auth import get_user_model, password_validation
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError

User = get_user_model()


class UserSerializer(serializers.ModelSerializer): # never converted to json and returned in response
    password = serializers.CharField(write_only=True) # write_only=True ensures never sent back in JSON
    password_confirmation = serializers.CharField(write_only=True)

    # validate function is going to:
    # check our passwords match
    # hash our passwords
    # add back to database
    def validate(self, data): # data comes from the request body
        print('DATA',data)
        # remove fields from request body and save to vars
        password = data.pop('password')
        password_confirmation = data.pop('password_confirmation')

        # check if they match
        if password != password_confirmation:
            raise ValidationError({'password_confirmation': 'do not match'})

        # checks if password is valid, comment this out so it works
        try:
            password_validation.validate_password(password=password)
        except ValidationError as err:
            print('VALIDATION ERROR')
            raise ValidationError({ 'password': err.messages })

        # hash the password, reassigning value on dict
        data['password'] = make_password(password)

        print('DATA ->', data)
        return data

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'id', 'email', 'password', 'password_confirmation')