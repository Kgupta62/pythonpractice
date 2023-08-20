from datetime import datetime,timedelta
today=datetime.now()
toda=today-timedelta(1)
tod=today+timedelta(1)
print(today,toda,tod)