format_float_ticks = lambda x, p: format(int(x), ',')


def get_timestamp_corresponding_to_day(day=0):
    start = 113500
    end = 150000

    start, end = 86400 * day + start, 86400 * day + end

    return start, end



