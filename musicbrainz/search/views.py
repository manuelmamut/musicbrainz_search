from django.shortcuts import render
from rest_framework import views
from rest_framework.response import Response
from rest_framework import serializers
from .serializers import releaseGroupSerializer, \
                         albumTypeReleaseGroupSerializer
from .utils import getYear
import musicbrainzngs


# Create your views here.


class releaseGroupView(views.APIView):

    def __init__(self):
        """We need to set the useragent for any request that we make to
        the musicbrainz webservice"""

        musicbrainzngs.set_useragent(
            "mamut_musicbrainz",
            "0.1",
            "https://github.com/manuelmamut/musicbrainz_search/",
        )

    def getReleaseGroupCount(self, release_group_id):
        """
        Helper function used to get the count of releases for a release-group by it's ID
        :param release_group_id: This is the id of the release-group
        :return release_count: The number of releases for that release-group
        """

        release_group_releases = musicbrainzngs.browse_releases(
            release_group=release_group_id)
        count = release_group_releases['release-count']

        return count


    def get(self, request):

        artist_id = request.GET.get('artist_id', None)
        offset = request.GET.get('offset', 0)
        limit = request.GET.get('limit', 50)

        if not artist_id:
            raise serializers.ValidationError(
                {"Request missing Artist ID":"You must pass an artist_id in your request"})

        #Let's get every release-group for the artist_id.
        release_group_list = musicbrainzngs.browse_release_groups(
            artist_id,
            release_type='album',
            offset=offset,
            limit=limit
            )
        release_group_list_count = len(release_group_list)

        print(release_group_list_count)
        #Now we can get our information and get it ready for serialize and return
        release_groups_info = [{'id':x['id'],
                               'title':x['title'],
                               'year':getYear(x['first-release-date']),
                               'release_count':self.getReleaseGroupCount(x['id'])
                               } for x in release_group_list['release-group-list']]
        print(release_group_list_count)
        albums = releaseGroupSerializer(release_groups_info, many=True).data

        #Let's set our pagination information
        next_offset= int(offset) + int(limit)
        showing = "{} to {}".format(offset,next_offset-1)

        response = albumTypeReleaseGroupSerializer({'albums':albums,
                                                    'next_offset':next_offset,
                                                    'showing':showing}).data

        return Response(response)
