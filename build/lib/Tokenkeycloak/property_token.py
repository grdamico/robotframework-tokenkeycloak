class PropertyToken:
    @property
    def typecall(self):
        return self.__typecall

    @typecall.setter
    def typecall(self, method):
        self.__typecall = method

    @property
    def baseurl(self):
        return self.__baseurl

    @baseurl.setter
    def baseurl(self, baseurl):
        self.__baseurl = baseurl

    @property
    def payload(self):
        return self.__payload

    @payload.setter
    def payload(self, payload):
        self.__payload = payload

    @property
    def headers(self):
        return self.__headers

    @headers.setter
    def headers(self, header):
        self.__headers = header