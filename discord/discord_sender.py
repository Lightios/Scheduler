from bot import run


def send():
    import requests

    # url_tutoring = "https://discord.com/api/webhooks/1175484080436031658/UJY19Fr-hNxhhrgD8ltGebT8egO9YDYEndYtPiZ_u91FnHVxfoRTrlt-ZhNEPCAFsoBb"
    url_eastside = "https://discord.com/api/webhooks/1184904437936967781/H6B861AyJqaRir93tjWEA7RcSl6TN1_-ILsOgO6F3UncJVvPwsrfVrwSbXaQoFocnJfI"

    # files_tutoring = {
    #     'payload_json': (None, '{"content": ""}'),
    #     'media': open('result.png', 'rb')
    # }

    files_eastside = {
        'payload_json': (None, '{"content": ""}'),
        'media': open('../result.png', 'rb')
    }

    # result_tutoring = requests.post(url_tutoring, files=files_tutoring)
    result_eastside = requests.post(url_eastside, files=files_eastside)

    run()
