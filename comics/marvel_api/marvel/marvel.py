import urllib
import json
import hashlib
import datetime
import requests
from .comic import ComicDataWrapper, Comic

DEFAULT_API_VERSION = 'v1'


class Marvel(object):
    """Marvel API class

    This class provides methods to interface with the Marvel API
    """

    def __init__(self, public_key, private_key):
        self.public_key = public_key
        self.private_key = private_key
        
    def _endpoint(self):
        return "http://gateway.marvel.com/%s/public/" % (DEFAULT_API_VERSION)

    def _call(self, resource_url, params=None):
        """
        Calls the Marvel API endpoint

        :param resource_url: url slug of the resource
        :type resource_url: str
        :param params: query params to add to endpoint
        :type params: str
        
        :returns:  response -- Requests response
        """
        
        url = "%s%s" % (self._endpoint(), resource_url)
        if params:
            url += "?%s&%s" % (params, self._auth())
        else:
            url += "?%s" % self._auth()
        return requests.get(url)

    def _params(self, params):
        """
        Takes dictionary of parameters and returns
        urlencoded string

        :param params: Dict of query params to encode
        :type params: dict
        
        :returns:  str -- URL encoded query parameters
        """
        return urllib.parse.urlencode(params)

    def _auth(self):
        """
        Creates hash from api keys and returns all required parametsrs
        
        :returns:  str -- URL encoded query parameters containing "ts", "apikey", and "hash"
        """
        ts = datetime.datetime.now().strftime("%Y-%m-%d%H:%M:%S")
        hash_string = hashlib.md5(("%s%s%s" % (ts, self.private_key, self.public_key)).encode('utf-8')).hexdigest()
        return "ts=%s&apikey=%s&hash=%s" % (ts, self.public_key, hash_string)

    def get_comic(self, id):
        """Fetches a single comic by id.
        
        get /v1/public/comics/{comicId}
        
        :param id: ID of Comic
        :type params: int
        
        :returns:  ComicDataWrapper
        Some Comic
        """
        
        url = "%s/%s" % (Comic.resource_url(), id)
        response = json.loads(self._call(url).text)
        return ComicDataWrapper(self, response)
                
    def get_comics(self, *args, **kwargs):
        """
        Fetches list of comics.

        get /v1/public/comics
                
        :returns:  ComicDataWrapper
        """

        response = json.loads(self._call(Comic.resource_url(), self._params(kwargs)).text)
        return ComicDataWrapper(self, response)


