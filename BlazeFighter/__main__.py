#RiZoeLXSpam By @TheRiZoeL

import asyncio
import sys
from sys import argv
import glob
from pathlib import Path
from RiZoeLXSpam.utils import load_plugins
import logging
from telethon import events
from . import Riz, Riz2, Riz3, Riz4, Riz5, Riz6, Riz7, Riz8, Riz9, Riz10, Riz11, Riz12, Riz13, Riz14, Riz15, Riz16, Riz17, Riz18, Riz19, Riz20 

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)


path = "RiZoeLXSpam/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))

print("RiZoeL Bot Spam Successfully deployed -!")
print("Enjoy! Do visit @RiZoeLX")

if len(argv) not in (1, 3, 4):
    try:
        Riz.disconnect()
    except Exception as e:
        pass
    try:
        Riz2.disconnect()
    except Exception as e:
        pass
    try:
        Riz3.disconnect()
    except Exception as e:
        pass
    try:
        Riz4.disconnect()
    except Exception as e:
        pass
    try:
        Riz5.disconnect()
    except Exception as e:
        pass
    try:
        Riz6.disconnect()
    except Exception as e:
        pass
    try:
        Riz7.disconnect()
    except Exception as e:
        pass
    try:
        Riz8.disconnect()
    except Exception as e:
        pass
    try:
        Riz9.disconnect()
    except Exception as e:
        pass
    try:
        Riz10.disconnect()
    except Exception as e:
        pass
    try:
        Riz11.disconnect()
    except Exception as e:
        pass
    try:
        Riz12.disconnect()
    except Exception as e:
        pass
    try:
        Riz13.disconnect()
    except Exception as e:
        pass
    try:
        Riz14.disconnect()
    except Exception as e:
        pass
    try:
        Riz15.disconnect()
    except Exception as e:
        pass
    try:
        Riz16.disconnect()
    except Exception as e:
        pass
    try:
        Riz17.disconnect()
    except Exception as e:
        pass
    try:
        Riz18.disconnect()
    except Exception as e:
        pass
    try:
        Riz19.disconnect()
    except Exception as e:
        pass
    try:
        Riz20.disconnect()
    except Exception as e:
        pass
else:
    try:
        Riz.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Riz2.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Riz3.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Riz4.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Riz5.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Riz6.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Riz7.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Riz8.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Riz9.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Riz10.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Riz11.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Riz12.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Riz13.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Riz14.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Riz15.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Riz16.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Riz17.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Riz18.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Riz19.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Riz20.run_until_disconnected()
    except Exception as e:
        pass
