import time
from injectable import injectable


@injectable
class ServiceHttpFlood:
    async def attack_epoch(self, epoch_number: int):
        print('ServiceHttpFlood.attack_epoch(): Started epoch #' + str(epoch_number))
        time.sleep(5)
        print('ServiceHttpFlood.attack_epoch(): Ended epoch #' + str(epoch_number))
