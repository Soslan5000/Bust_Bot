from string import Template

def getRegData(user, title, name):
    t = Template(
        '$title*$name*'
        '\nВаш текущий птс: *$intial_pts*'
        '\nЖелаемый птс: *$final_pts*'
        '\nЖелаемое время выполнения: *$lead_time* дней'
        '\nЖелаемый способ буста: *$method*'
        '\n\nСтоимость буста: *$final_sum*'
    )

    return t.substitute({
        'title': title,
        'name': name,
        'intial_pts': user.initial_pts,
        'final_pts': user.final_pts,
        'lead_time': user.lead_time,
        'method': user.method,
        'final_sum': user.final_sum
    })