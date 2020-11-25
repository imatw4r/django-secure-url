from itertools import groupby

from django.db.models import Count
from django.http.response import JsonResponse

from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework import permissions
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin

from secure_resource.models import SecureElement, ElementRedirect
from .permissions import IsPasswordCorrect
from .serializers import (
    SecureUrlSerializer,
    SecureFileSerializer,
    FileRedirectSerializer,
    UrlRedirectSerializer,
)


def update_daily_count(daily_count, redirect):
    daily_count = {**daily_count}
    if redirect["redirect_type"] == ElementRedirect.FILE:
        daily_count["files"] = redirect["count"]
    else:
        daily_count["links"] = redirect["count"]
    return daily_count


class ElementRedirectListStatisticsViewSet(GenericViewSet, ListModelMixin):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = ElementRedirect.objects.filter(visited__gte=1)

    def list(self, request):
        qs = (
            self.get_queryset()
            .values("created_at", "redirect_type")
            .annotate(count=Count("created_at"))
            .order_by("created_at", "redirect_type")
        )

        counts = {}
        for date, group in groupby(qs, lambda redirect: redirect["created_at"]):
            daily_count = {
                "links": 0,
                "files": 0,
            }
            for redirect in group:
                daily_count = update_daily_count(daily_count, redirect)
            counts[str(date)] = daily_count
        return JsonResponse(counts)


class SecureUrlViewSet(ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = SecureElement.objects.filter(redirect__redirect_type="URL")
    serializer_class = SecureUrlSerializer


class SecureFileViewSet(ModelViewSet):
    parser_classes = (FormParser, MultiPartParser)
    permission_classes = (permissions.IsAuthenticated,)
    queryset = SecureElement.objects.filter(source_url__isnull=True)
    serializer_class = SecureFileSerializer


class FileRedirectRetrieveModelViewSet(RetrieveModelMixin, GenericViewSet):
    permission_classes = (IsPasswordCorrect,)
    queryset = ElementRedirect.objects.filter(redirect_type=ElementRedirect.FILE)
    serializer_class = FileRedirectSerializer


class UrlRedirectRetrieveModelViewSet(RetrieveModelMixin, GenericViewSet):
    permission_classes = (IsPasswordCorrect,)
    queryset = ElementRedirect.objects.filter(redirect_type=ElementRedirect.URL)
    serializer_class = UrlRedirectSerializer
