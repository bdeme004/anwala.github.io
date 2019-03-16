import datetime

test_date = datetime.datetime.fromisoformat("")
now = datetime.datetime.today()
print((now - test_date).days)
