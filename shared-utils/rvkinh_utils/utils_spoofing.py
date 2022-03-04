from typing import Dict, Any
from injectable import injectable, autowired, Autowired
from tekleo_common_utils import UtilsRandom


@injectable
class UtilsSpoofing:
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
