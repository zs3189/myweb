# encoding: utf-8
'''
@author: zhushen
@contact: 810909753@q.com
@time: 2018/2/6 9:45
'''

from rest_framework import viewsets, status
from bid.api.serializers import Bid_actionSerializer, Bid_handerSerializer, Bid_auctionSerializer
from bid.models import Bid_action, Bid_auction, Bid_hander, query_auction_by_args, query_auction_by_url
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
import django_filters
import json
from rest_framework.decorators import api_view


class Bid_handerViewSet(viewsets.ModelViewSet):
    queryset = Bid_hander.objects.all()
    serializer_class = Bid_handerSerializer
    permission_classes = (permissions.IsAuthenticated,)  #permissions.AllowAny  注册设置为这个


class Bid_actionViewSet(viewsets.ModelViewSet):
    queryset = Bid_action.objects.all()
    serializer_class = Bid_actionSerializer
    permission_classes = (permissions.IsAuthenticated,)
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_fields = ('diff', 'ahead_price')




class Bid_auctionViewSet(viewsets.ModelViewSet):
    queryset = Bid_auction.objects.all()  #pk = id
    serializer_class = Bid_auctionSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_fields = ('auction_name', 'ID_number')


##serverside查询
class Bid_auction_serversideViewSet(viewsets.ModelViewSet):
    queryset = Bid_auction.objects.all()
    serializer_class = Bid_auctionSerializer

    ##用GET来实现批量删除
    def list(self, request, **kwargs):
        try:
            deleteorget = request.GET.get('data', None)
            if deleteorget == None:
                auctions = query_auction_by_args(request.GET)
                serializer = Bid_auctionSerializer(auctions['items'], many=True)
                result = dict()
                result['rows'] = serializer.data
                result['total'] = auctions['total']
                return Response(result, status=status.HTTP_200_OK, template_name=None, content_type=None)
            else:
                data = json.loads(deleteorget)  ##转json
                auctions = query_auction_by_url(data)
                auctions.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response(e, status=status.HTTP_404_NOT_FOUND, template_name=None, content_type=None)

    def update(self, request, *args, **kwargs):
        try:
            data = request.data
            auction = Bid_auction.objects.get(pk=data['pk'])
            description = data['description']  # 描述来源
            auction_name = data['auction_name']  # 标书姓名
            ID_number = data['ID_number']  # 身份证号
            Bid_number = data['Bid_number']  # 标书号
            Bid_password = data['Bid_password']  # 密码
            status_ = data['status']  # 标书状态  避免重名
            count = data['count']  # 参拍次数
            expired_date = data['expired_date']  # 过期时间
            auction.update(description=description, auction_name=auction_name, ID_number=ID_number,
                                         Bid_number=Bid_number, Bid_password=Bid_password, status=status_,
                                         count=count, expired_date=expired_date)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def Bid_auction_manage(request):
    """
    Retrieve, update or delete a code snippet. """
    if request.method == 'GET':
        try:
            auctions = query_auction_by_args(request.GET)
            serializer = Bid_auctionSerializer(auctions['items'], many=True)
            result = dict()
            result['rows'] = serializer.data
            result['total'] = auctions['total']
            return Response(result, status=status.HTTP_200_OK, template_name=None, content_type=None)
        except Exception as e:
            return Response(e, status=status.HTTP_404_NOT_FOUND, template_name=None, content_type=None)
    elif request.method == 'PUT':
        try:
            data = request.GET
            pk = data.get('id')
            serializer = Bid_auction.objects.get(pk=pk)
            serializer = Bid_auctionSerializer(serializer, data=data)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
        except :
            return Response(status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'DELETE':
        try:
            data = request.GET.get('data')
            data = json.loads(data)  ##转json
            auctions = query_auction_by_url(data)
            auctions.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'POST':
        try:
            data = request.POST
            serializer = Bid_auctionSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)



    # def destroy(self, request, **kwargs):
    #     try:
    #         auctions = query_auction_by_url(request.data)['data']
    #         auctions = json.loads(auctions) #转json
    #         print(auctions)
    #         serializer = Bid_auction(auctions, many=True)
    #         serializer.delete()
    #         return Response(status=status.HTTP_204_NO_CONTENT)
    #     except:
    #         return Response(status=status.HTTP_404_NOT_FOUND)




# try:
#     snippet = Snippet.objects.get(pk=pk)
# except Snippet.DoesNotExist:
#     return Response(status=status.HTTP_404_NOT_FOUND)
#
# if request.method == 'GET':
#     serializer = SnippetSerializer(snippet)
#     return Response(serializer.data)
#
# elif request.method == 'PUT':
#     serializer = SnippetSerializer(snippet, data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# elif request.method == 'DELETE':
#     snippet.delete()
#     return Response(status=status.HTTP_204_NO_CONTENT)