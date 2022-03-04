from typing import List, Dict, Any
import requests
from injectable import injectable, autowired, Autowired
from tekleo_common_utils import UtilsRandom
from rvkinh_message_protocol import HttpResponse


@injectable
class ServiceHttp:
    @autowired
    def __init__(self, utils_random: Autowired(UtilsRandom)):
        self.utils_random = utils_random

    def get_header(self) -> Dict[str,Any]:
        return {
            'User-Agent': self.utils_random.get_random_user_agent(),
            'X-Forwarded-For': self.utils_random.get_random_ip(),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-us,en;q=0.5',
            'Accept-Encoding': 'gzip,deflate',
            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7',
            'Keep-Alive': '115',
            'Connection': 'keep-alive',
        }

    def http_get(self, url: str, headers: Dict = {}, proxies: Dict = {}, timeout: int = 10) -> HttpResponse:
        try:
            response = requests.get(url, headers=headers, proxies=proxies, timeout=timeout)
        except:
            print('ServiceHttp.http_get(): WARNING!!!! Request on ' + url + ' failed')
            return HttpResponse(-1, None, None)

        response_json = None
        try:
            response_json = response.json()
        except:
            pass
        response_content = None
        try:
            response_content = response.content
        except:
            pass

        print('ServiceHttp.http_get(): Returned code ' + str(response.status_code) + ' on ' + url)
        return HttpResponse(response.status_code, response_json, response_content)
