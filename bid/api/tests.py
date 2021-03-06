import json

from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from requests.auth import HTTPBasicAuth

from rest_framework import status
from bid.models import Identify



# class UserLogoutAPIViewTestCase(APITestCase):
#     url = reverse("api_bid: ic_mange")
#
#     def setUp(self):
#         self.username = "john"
#         self.email = "john@snow.com"
#         self.password = "you_know_nothing"
#         self.user = User.objects.create_user(self.username, self.email, self.password)
#         self.token = Token.objects.create(user=self.user)
#         self.client.auth = HTTPBasicAuth('user', 'pass')
#         self.client.headers.update({'x-test': 'true'})
#
#
#     def test_getic(self):
#         datas = {'format': 'json', }
#         response = self.client.get(self.url, data=datas)
#         csrftoken = response.cookies['csrftoken']
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(User.objects.count(), 1)
#         self.assertEqual(User.objects.get().name, 'DabApps')


class guopaiurlAPIViewTestCase(APITestCase):
    get_guopaiurl = "/bid/api/get_guopaiurl/"
    # monitest = reverse("api_bid: monitest")
    get_remotetime = "/bid/api/get_remotetime/"
    # bid_firstprice = reverse("api_bid: bid_firstprice")
    # bid_logout = reverse("api_bid: bid_logout")
    # bid_keeplogin = reverse("api_bid: bid_keeplogin")

    def setUp(self):
        self.identify_code = Identify.objects.create(
            identify_code='6454'
        )

    def test_get_guopaiurl(self):
        data1 = {}
        response1 = self.client.get(self.get_guopaiurl, data=data1)
        self.assertNotEqual(response1.status_code, status.HTTP_200_OK)
        print(self.identify_code.identify_code)
        data2 = {'type': 'identify_code', 'identify_code': self.identify_code.identify_code,
                 'diskid': 'none' }
        response2 = self.client.get(self.get_guopaiurl, data=data2)
        self.assertNotEqual(response2.status_code, status.HTTP_200_OK)

    def test_monitest(self):
        pass

    def test_get_remotetime(self):
        response = self.client.get(self.get_remotetime)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_bid_firstprice(self):
        pass

    def test_bid_logout(self):
        pass

    def test_keeplogin(self):
        pass







##101.87.221.219