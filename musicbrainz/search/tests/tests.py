from django.test import TestCase, Client
from django.urls import reverse
from urllib.parse import urlencode

class TestSearchViews(TestCase):
    """Test for the search app endpoints"""

    def setUp(self):
        pass

    def test_can_get_release_groups(self):
        """We check if the request return the information expected"""
        url = reverse("search:release-groups")
        get_vars = {'artist_id':'65f4f0c5-ef9e-490c-aee3-909e7ae6b2ab',
                    'offset':10,
                    'limit':2
                    }
        url_get = "{}?{}".format(url, urlencode(get_vars))
        print(url_get)
        response = self.client.get(url_get)
        assert response.status_code == 200, \
            "Wanted 200 got: {}" . format(
                response.status_code)
        assert len(response.json()) == 5, \
            "We must have 5 keywords, {} found". format( #here we confirm our response information
            len(response.json()))
        assert len(response.json()['albums']) == 2 , \
            "We ask for 2 albums, {} found". format( #here we confirm that we get what we ask
            len(response.json()['albums']))
        assert type(response.json()['release_group_count']) == int , \
            "release-group-count is an integer, {} found". format( #here we confirm the type of the info received
            type(response.json()['release-group-count']))

        assert 'title' in response.json()['albums'][0] , "title not found in albums dict"
        assert 'id' in response.json()['albums'][0] , "id not found in albums dict"
        assert 'year' in response.json()['albums'][0] , "year not found in albums dict"
        assert 'release_count' in response.json()['albums'][0] , "release_count not found in albums dict"
