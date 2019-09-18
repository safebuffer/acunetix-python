#!/usr/bin/env python3
from requests import get as http_get_request
from requests import post as http_post_request
import requests
requests.packages.urllib3.disable_warnings()
import json

class ACUX(object):
    def __init__(self, host=None, api=None, timeout=10):
        self.apikey = api
        self.host = str("{}{}".format("https://" if "https://" not in host else "",host))
        self.timeout = timeout
        
    def __headers(self):
        return {"X-Auth":self.apikey,"content-type": "application/json"} if self.apikey else None

    def __get_request(self,endpoint=None):
        return http_get_request(str("{}{}".format(self.host, endpoint if endpoint else "/")),headers=self.__headers(),timeout=self.timeout,verify=False)
    
    def __post_request(self,endpoint=None,data=None):
        return http_post_request(str("{}{}".format(self.host, endpoint if endpoint else "/")),data=json.dumps(data),headers=self.__headers(),timeout=self.timeout,verify=False)

    def __json_return(self,data):
        return json.loads(data)

    def scans(self):
        req = self.__get_request(endpoint="/api/v1/scans")
        return self.__json_return(req.text)

    def info(self):
        req = self.__get_request(endpoint="/api/v1/info")
        return self.__json_return(req.text)

    def add_target(self,target=None):
        req = self.__post_request(endpoint="/api/v1/targets",data={"address":target,"description":"xxxx","criticality":"10"})
        return self.__json_return(req.text)

    def add_and_start(self,target=None):
        target_id = self.add_target(target=target)['target_id']
        payload = {
            "target_id":str(target_id),
            "profile_id":"11111111-1111-1111-1111-111111111111",
            "schedule":    
                {"disable":False,
                "start_date":None,
                "time_sensitive":False
                }
            }

        req = self.__post_request(endpoint="/api/v1/scans",data=payload)
        return self.__json_return(req.text)