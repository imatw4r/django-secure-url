from rest_framework import serializers
from secure_resource.models import ElementRedirect


class RedirectDailyCountSerializer(serializers.Serializer):
    redirect_type = serializers.CharField(
        required=True, choices=((ElementRedirect.URL, ElementRedirect.FILE))
    )
    date = serializers.DateTime(required=True)
    count = serializers.IntegerField(required=True)


s = RedirectDailyCountSerializer(data={})
print(s.is_valid())