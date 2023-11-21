# This file will get replaced in the review step with real sms functionality.


import logging
from dataclasses import dataclass

@dataclass
class SMS:
    phone_number: str
    message: str

    def send(self):
        logging.info(f'Sending {self.message} to {self.phone_number}')
