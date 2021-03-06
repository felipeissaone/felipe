from mathias.user.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('team_id', 'name', 'status', 'real_name', 'first_name', 'last_name',
                  'title', 'email', 'image_24', 'image_32', 'image_48', 'image_72',
                  'image_192', 'image_original', 'create_at')
