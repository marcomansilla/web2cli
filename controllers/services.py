# coding=utf-8

def api():
    from apimaker import APIMaker
    api = APIMaker(db)

    # api people
    api.add_policy('person','GET')
    api.add_policy('person','POST')
    api.add_policy('person','PUT')
    api.add_policy('person','DELETE')

    return api.process()
