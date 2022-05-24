from application import Serializer

###### USER SERIALIZER #####
class UserSerializer(Serializer):
    class Meta:
        # Fields to expose
        fields = ('username')
        # you can add any other member of class user in fields

#Return the user data in json format
def get_user_serialized(user):
    return UserSerializer(user).data