from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from app.filter import ClothesFilterSet, LimitFilter
from app.models import Clothes
from app.paginations import MyPageNumberPagination, MyLimitPagination, MyCoursePagination
from app.serializers import UserModelSerializer, ClothesModelSerializer
from utils.response import APIResponse
from app.authentication import JWTAuthentication

class UserDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]
    # authentication_classes = [JWTAuthentication]
    authentication_classes = [JSONWebTokenAuthentication]

    def get(self, request, *args, **kwargs):
        return APIResponse(results={"username": request.user.username})


class LoginAPIView(APIView):

    authentication_classes = []
    permission_classes = []

    def post(self, request, *args, **kwargs):
        user_ser = UserModelSerializer(data=request.data)
        user_ser.is_valid(raise_exception=True)

        return APIResponse(data_message="ok", token=user_ser.token, results=UserModelSerializer(user_ser.obj).data)
class ClothesListAPIView(ListAPIView):
    queryset = Clothes.objects.all()
    serializer_class = ClothesModelSerializer

    filter_backends = [SearchFilter, OrderingFilter, LimitFilter, DjangoFilterBackend]
    search_fields = ["name", "price"]
    ordering = ["price"]

    pagination_class = MyPageNumberPagination
    # pagination_class = MyLimitPagination
    # pagination_class = MyCoursePagination

    filter_class = ClothesFilterSet