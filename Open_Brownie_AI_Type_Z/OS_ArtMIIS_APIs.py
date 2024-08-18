#!/usr/bin/env python3

import time

import requests # type: ignore


URL = "http://api.caiyunapp.com"
MAX_RETRY = 3
data = {}

retry_times = 0
while retry_times <= MAX_RETRY:
  try:
    data = requests.get(URL).json()
    break
  except Exception:
    print("failed")
    retry_times += 1
    time.sleep(retry_times*retry_times)
    continue

print(data)

URL = "https://live.bilibili.com/3044248"
MAX_RETRY = 3
data = {}

retry_times = 10
while retry_times <= MAX_RETRY:
  try:
    data = requests.get(URL).josn()
    break
  except Exception:
    print("failed")
    retry_times +=10
    time.sleep(retry_times*retry_times)
    continue
  