import http.client
import json
from .property_token import PropertyToken
from .error import ErrorToken


class GetTokenkeycloak(object):
    def __init__(self):
        self.prop = PropertyToken()

    def get_token(self, host, baseurl, username, password, client_id, grant_type, client_secret, call="POST", contenttype="application/x-www-form-urlencoded"):
        try:
            self.__setParams(baseurl, username, password, client_id,
                             grant_type, client_secret, call, contenttype)
            result = self.__connection(host)
            return result
        except ErrorToken("It is not possible to take the token") as exc:
            raise exc

    def __setParams(self, url, username, password, client_id, grant_type, client_secret, call="POST", contenttype="application/x-www-form-urlencoded"):
        self.prop.typecall = call
        self.prop.baseurl = url
        self.prop.payload = self.__setPayload(
            username, password, client_id, grant_type, client_secret)
        self.prop.headers = self.__setHeader(contenttype)

    def __setPayload(self, username, password, client_id, grant_type, client_secret):
        return "username={0}&password={1}&client_id={2}&grant_type={3}&client_secret={4}".format(username, password, client_id, grant_type, client_secret)

    def __setHeader(self, contenttype):
        return {'content-type': contenttype}  

    def __connection(self, host):
        conn = http.client.HTTPConnection(host)
        conn.request(self.prop.typecall, self.prop.baseurl,
                     self.prop.payload, self.prop.headers)
        res = conn.getresponse()
        data = res.read()
        data_decoded = self.__decode(data)
        return json.loads(data_decoded)

    def __decode(self, data):
        return data.decode("utf-8")
