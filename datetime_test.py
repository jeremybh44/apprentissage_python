from datetime import datetime, timedelta

from dateutil.relativedelta import relativedelta

# disponible a partir de python 3.9
# from zoneinfo import ZoneInfo

# date et heure actuel
now = datetime.now()

# rendre un objet datetime naive -> aware (specifier le fuseau horaire)
# now_in_vancouver = datetime.now(tz=ZoneInfo("America/Vancouver"))
# print(now_in_vancouver)

# Changer le fuseau horaire d'un datetime
# now_in_paris = now_in_vancouver.astimezone(ZoneInfo("Europe/Paris"))

# Pour faire des opérations avec différent datetime, bien être en tz
# UTC pour que la prise en compte du fuseau horaire soit faite

now_in_15_days = now + timedelta(days=15)

now_in_2_month = now + relativedelta(months=2)
