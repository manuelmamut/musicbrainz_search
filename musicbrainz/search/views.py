from django.shortcuts import render
from rest_framework import views
from rest_framework.response import Response
from rest_framework import serializers
from .serializers import releaseGroupSerializer, \
                         albumTypeReleaseGroupSerializer
from .utils import getYear, getPaginationInfo
from datetime import datetime
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

    def get(self, request):

        release_group_list = []
        artist_id = request.GET.get('artist_id', None)
        offset = int(request.GET.get('offset', 0))
        limit = int(request.GET.get('limit', 50))

        if not artist_id:
            raise serializers.ValidationError(
                {"Request missing Artist ID":"You must pass an artist_id in your request"})

        #Let's get every release-group for the artist_id.
        #We should consider that our limit could higher than the musicbrainz max limit

        release_group_list, release_group_count = self.getReleaseGroupInfo(artist_id, 
                                                                    'album', 
                                                                    offset, 
                                                                    limit)

        print(len(release_group_list))

        #Now we can get our information and get it ready for serialize and return
        release_groups_info = [{'id':x['id'],
                                   'title':x['title'],
                                   'year':getYear(x['first-release-date']),
                                   'release_count':self.getReleaseCount(x['id'])
                                   } for x in release_group_list]


        albums = releaseGroupSerializer(release_groups_info, many=True).data

        #Let's set our pagination information
        next_offset, showing = getPaginationInfo(offset, limit, release_group_count)
        response = albumTypeReleaseGroupSerializer({
                                            'albums':albums,
                                            'next_offset':next_offset,
                                            'showing':showing,
                                            'release_group_count':release_group_count,
                                            'date':datetime.now()}).data

        return Response(response)


    def getReleaseCount(self, release_group_id):
        """
        Helper function used to get the count of releases for a release-group by it's ID
        :param release_group_id: This is the id of the release-group
        :return release_count: The number of releases for that release-group
        """

        try:
            release_group_releases = musicbrainzngs.browse_releases(
                release_group=release_group_id)
            count = release_group_releases['release-count']
        except:
            raise serializers.ValidationError(
                {"Too much music":"Seems like everybody wants to know how many albums blink 182 released, \
                    At least they are not looking for Britney. Give us a second a try again"})

        return count


    def getReleaseGroupInfo(self, artist_id, r_type, offset, limit):
        """
        Helper function used to get the information and count of the releases groups. 
        We use this basically because we want to handle our custom pagination if limit is higher
        than the limit set by mbz_max_limit
        :param artist_id: This is the MBID for the artist
        :param r_type: This is release type
        :param offset: where we start counting for our pagination
        :param limit: where to stop counting
        :return release_group_list: The list of the release-groups found
        :return release_count: The number of release-groups returned
        """

        mbz_max_limit = 100 #TODO put in config
        if limit > mbz_max_limit:
            #Here we get the first chunk below mbz_max_limit
            release_group = musicbrainzngs.browse_release_groups(artist_id,
                                                            release_type=r_type,
                                                            offset=offset,
                                                            limit=limit)
            release_group_list = release_group['release-group-list']
            release_group_count = release_group['release-group-count']
            
            #Here we get the rest of the info
            if offset + mbz_max_limit < release_group_count:
                release_group_list_complement = musicbrainzngs.browse_release_groups(
                                                                            artist_id,
                                                                            release_type = r_type,
                                                                            offset=offset+mbz_max_limit, 
                                                                            limit=limit-mbz_max_limit
                                                                            )
                #Here we merge the two list chunks
                release_group_list += release_group_list_complement['release-group-list'] 
                                                            
        else:
            release_group = musicbrainzngs.browse_release_groups(artist_id,
                                                            release_type=r_type,
                                                            offset=offset,
                                                            limit=limit)
            release_group_list = release_group['release-group-list']
            release_group_count = release_group['release-group-count']
        return release_group_list, release_group_count

