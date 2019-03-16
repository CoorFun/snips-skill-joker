#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from hermes_python.hermes import Hermes
from hermes_python.ontology import *
import io
import requests

def fetch_joke(hermes, intentMessage):
    res = requests.get("http://api.icndb.com/jokes/random/").json()

    if res.get('type') == 'success':
        say = str(res.get('value').get('joke')).replace('&quot;','')
        hermes.publish_end_session(intentMessage.session_id, say)
    else:
        hermes.publish_end_session(intentMessage.session_id, "")

if __name__ == "__main__":
    with Hermes("localhost:1883") as h:
        h.subscribe_intent("coorfang:askJoke", fetch_joke) \
         .start()