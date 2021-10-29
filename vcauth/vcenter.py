import requests
from requests.structures import CaseInsensitiveDict
import base64

class Vcenter:
    vcenter_url = 'https://10.5.0.77/rest/com/vmware/cis/session'
    def get_session(self, email, password):
        self.email = email
        self.password = password

        c = self.email + ':' + self.password
        encrypted_c = c.encode('ascii')
        baseAuth = (self.email, self.password)
        headers = CaseInsensitiveDict()
        """headers = {
            'Accpet': 'application/json',
            'Authorization' : 'Basic ' + str(encrypted_c),
        }"""
        s = requests.session()
        s.verify = False

        r = s.request('POST', self.vcenter_url, auth=baseAuth)
        return r

    def drop_session(self):
        s = requests.session()
        s.verify = False
        r = s.request('DELETE', self.vcenter_url)
        return r

