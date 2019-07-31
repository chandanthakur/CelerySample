from __future__ import absolute_import, unicode_literals
from .tasks import add

for i in range(10000):
    add.delay(100,23)