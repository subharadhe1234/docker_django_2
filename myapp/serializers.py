from django.contrib.auth.models import Group, User
from rest_framework import routers, serializers, viewsets

class UserSerializer(serializers.HyperlinkedModelSerializer):
    groups = serializers.HyperlinkedRelatedField(
    many=True,
    queryset=Group.objects.all(),
    view_name='group-detail',  # This view_name must match the one in your URLs configuration
    lookup_field='pk'  # Ensure this matches the lookup field used in the Group view
)
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
        extra_kwargs = {
            'url': {'view_name': 'group-detail', 'lookup_field': 'pk'}}