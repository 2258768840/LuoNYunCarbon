retry_times = 0
while retry_times <= MAX_RETRY:
  try:
    data = requests.get(URL).json()
    break
  except Exception:
    print("failed")
    retry_times += 1
    time.sleep(retry_times*retry_times)
    continues