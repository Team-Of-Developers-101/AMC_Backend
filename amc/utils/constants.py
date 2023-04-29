"""Code constants"""

import os
import random
import string


class _Const():
    """String constants"""
    @property
    def secret_key(self):
        """secret_key"""
        secret = ''.join(  # generating random secret-key
            random.choice(
                string.ascii_letters
            ) for i in range(32)
        )
        return secret

    @property
    def environ(self):
        """Envrionment variable"""
        env = os.getenv("ENVIRONMENT")
        return env
