import time as t


def s(num: int) -> str:
    return '' if num == 1 else 's'


def date_time(time: str) -> str:
    ts = t.strptime(time, '%d.%m.%Y %H:%M')
    return t.strftime(f'%-d %B %Y year %-H hour{s(ts.tm_hour)} %-M minute{s(ts.tm_min)}', ts)
