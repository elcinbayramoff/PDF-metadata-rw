import datetime
import pytz

def back_formatter(date):
    date_time_obj = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S%z')
    formatted_str = 'D:' + date_time_obj.strftime('%Y%m%d%H%M%S') + '+00\'00\''
    return formatted_str

def get_utc_offset():
    utc_offset = datetime.datetime.now(datetime.timezone.utc).astimezone().utcoffset()
    utc_offset_hours = utc_offset.total_seconds() / 3600
    return int(utc_offset_hours)

def formatter(time):
    year,month,day,hour,minute,second = time[2:6],time[6:8],time[8:10],time[10:12],time[12:14],time[14:16]
    return {
        'year':year,
        'month':month,
        'day':day,
        'hour':hour,
        'minute':minute,
        'second':second,
    }
def toLocalUTC(year,month,day,hour,minute,second):
    dt = datetime.datetime(year, month, day, hour, minute, second)
    utc = pytz.utc
    utc_local = pytz.timezone(f'Etc/GMT-{get_utc_offset()}')
    dt_utc = dt.replace(tzinfo=utc)
    dt_utc_local = dt_utc.astimezone(utc_local)
    return dt_utc_local
        