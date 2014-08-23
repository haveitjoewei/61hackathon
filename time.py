#import dateutil.parser as dparser

# def closesttime(stationname):
#     """
#     >>>closesttime("Downtown Berkeley Bart Station")
#     "7:00"
#     """
#     nowtime = datetime.datetime.now()
#     dparser.parse(nowtime, fuzzy=True, ignoretz=True)
#     for i in range(0, 30):
#         nexttime = allTimes[stationname][i]
#         dparser.parse(nexttime, fuzzy=True, ignoretz=True)
#         if not nowtime>nexttime:
#             break
#     return nexttime