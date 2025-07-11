import threading

from hpa import _app

_apps = {}
_apps_lock = threading.RLock()
_DEFAULT_APP_NAME = 'DEFAULT'


def initialize_app(
    appid, 
    appsecret, 
    token_server='https://oauth-login.cloud.huawei.com/oauth2/v2/token',
    push_open_url='https://push-api.cloud.huawei.com'
):
    """
        Initializes and returns a new App instance.
        :param appid: appid parameters obtained by developer alliance applying for Push service
        :param appsecret: appsecret parameters obtained by developer alliance applying for Push service
        :param token_server: Oauth server URL
        :param push_open_url: push open API URL
    """
    app = _app.App(appid, appsecret, token_server=token_server, push_open_url=push_open_url)

    with _apps_lock:
        if appid not in _apps:
            _apps[appid] = app

        """set default app instance"""
        if _apps.get(_DEFAULT_APP_NAME) is None:
            _apps[_DEFAULT_APP_NAME] = app


def get_app(appid=None):
    """
        get app instance
        :param appid: appid parameters obtained by developer alliance applying for Push service
        :return: app instance
        Raise: ValueError
    """
    if appid is None:
        with _apps_lock:
            app = _apps.get(_DEFAULT_APP_NAME)
            if app is None:
                raise ValueError('The default Huawei app is not exists. '
                                 'This means you need to call initialize_app() it.')
            return app

    with _apps_lock:
        if appid not in _apps:
            raise ValueError('Huawei app id[{0}] is not exists. '
                             'This means you need to call initialize_app() it.'.format(appid))

        app = _apps.get(appid)
        if app is None:
            raise ValueError('The app id[{0}] is None.'.format(appid))
        return app
