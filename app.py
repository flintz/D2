__author__ = 'flintz'
#import sys
# $ export D2_API_KEY=
import dota2api
api = dota2api.Initialise()
match = api.get_match_details(match_id=1000193456)




