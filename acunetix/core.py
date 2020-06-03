#!/usr/bin/env python3
import requests
requests.packages.urllib3.disable_warnings()
import json


class AXException(Exception):
    HTTP_ERROR = "HTTP Error "
    AUTH_ERROR = "Wrong API Key"



class Acunetix(object):
    def __init__(self, host=None, api=None, timeout=20):
        self.apikey = api
        self.host = str("{}{}".format("https://" if "https://" not in host else "",host))
        self.timeout = timeout
        self.headers = {
                "X-Auth":self.apikey,
                "content-type": "application/json",
                "User-Agent": "Acunetix"
            }
    
    def __json_return(self,data):
        try:
            return json.loads(data)
        except:
            pass
        
    def __send_request(method="get", endpoint="" , data=None):
        request_call = getattr(requests, method)
        url = str("{}{}".format(self.host, endpoint if endpoint else "/"))
        try:
            request = request_call(url, headers=self.headers, timeout=self.timeout, data=json.dumps(data), verify=False)
            return self.__json_return(request.text)
        except:
            pass

    def info(self):
        return self.__send_request(method="get", endpoint="/api/v1/info")

    def targets(self):
        return self.__send_request(method="get", endpoint="/api/v1/targets?pagination=50")

    def add_target(self,target):
        target_address = target if 'http://' or 'https://' in target else "http://{}".format(target)
        data = {"address":target_address, "description":"Sent from Acunetix-Python","criticality":"10"}
        return self.__send_request(method="post", endpoint="/api/v1/targets" , data=data)

    def delete_target(self, target_id):
        return self.__send_request(method="delete", endpoint="/api/v1/targets/{}".format(target_id))

    def scans(self):
        return self.__send_request(method="get", endpoint="/api/v1/scans")

    def delete_all_targets(self):
        targets = self.targets()
        if len(targets['targets']):
            for target in targets['targets']:
                self.delete_target(i['target_id'])
        else:
            break
