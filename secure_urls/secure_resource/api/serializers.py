from rest_framework import serializers

from secure_resource.models import ElementRedirect, SecureElement


class SecureUrlSerializer(serializers.ModelSerializer):
    redirect_path = serializers.SerializerMethodField("get_redirect_path")

    class Meta:
        model = SecureElement
        fields = ("id", "source_url", "redirect_path", "password")
        read_only_fields = ("password",)

    def get_redirect_path(self, instance):
        redirect = instance.redirect
        if not redirect:
            return None
        return redirect.get_absolute_url()


class SecureFileSerializer(serializers.ModelSerializer):
    redirect_path = serializers.SerializerMethodField("get_redirect_path")

    class Meta:
        model = SecureElement
        fields = (
            "id",
            "source_file",
            "redirect_path",
            "password",
        )
        read_only_fields = ("password",)

    def get_redirect_path(self, instance):
        redirect = instance.redirect
        if not redirect:
            return None
        return redirect.get_absolute_url()


class FileRedirectSerializer(serializers.ModelSerializer):
    source = serializers.CharField(source="element.source_file")

    class Meta:
        model = ElementRedirect
        fields = ("id", "expires_at", "source")


class UrlRedirectSerializer(serializers.ModelSerializer):
    source = serializers.CharField(source="element.source_url")

    class Meta:
        model = ElementRedirect
        fields = ("id", "expires_at", "source")
