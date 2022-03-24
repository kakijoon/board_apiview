# 데이터 처리
from .models import board_api
from .serializer import Board_apiSerializer

# APIView를 사용하기 위해 import
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework import viewsets


# board_api의 목록을 보여주는 역할
class BoardList(APIView):
    # board list를 보여줄 때
    def get(self, request):
        board_apis = board_api.objects.all()
        # 여러 개의 객체를 serialization하기 위해 many=True로 설정
        serializer = Board_apiSerializer(board_apis, many=True)
        return Response(serializer.data)

    # 새로운 board_api 글을 작성할 때
    def post(self, request):
        # request.data는 사용자의 입력 데이터
        serializer = Board_apiSerializer(data=request.data)
        if serializer.is_valid():  # 유효성 검사
            serializer.save()  # 저장
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# board_api의 detail을 보여주는 역할
class BoardDetail(APIView):
    # board_api 객체 가져오기
    def get_object(self, pk):
        try:
            return board_api.objects.get(pk=pk)
        except board_api.DoesNotExist:
            raise Http404

    # board_api의 detail 보기
    def get(self, request, pk, format=None):
        board_apis = self.get_object(pk)
        serializer = Board_apiSerializer(board_apis)
        return Response(serializer.data)

    # board_api 수정하기
    def put(self, request, pk, format=None):
        board_apis = self.get_object(pk)
        serializer = Board_apiSerializer(board_apis, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # board 삭제하기
    def delete(self, request, pk, format=None):
        board_apis = self.get_object(pk)
        board_apis.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)