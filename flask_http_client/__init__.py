import requests
from flask import g
from requests.auth import HTTPBasicAuth


class HTTPClient(object):
    def __init__(
        self,
        app=None,
        base_url=None,
        username=None,
        password=None,
        verify=None,
        g_session_key=None,
        config_prefix="HTTP_CLIENT",
    ):
        self.base_url = base_url
        self.username = username
        self.password = password
        self.verify = verify
        self.g_session_key = g_session_key
        self.config_prefix = config_prefix

        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        if self.base_url is None:
            self.base_url = app.config[f"{self.config_prefix}_BASE_URL"]
        if self.username is None:
            self.username = app.config.get(f"{self.config_prefix}_USERNAME")
        if self.password is None:
            self.password = app.config.get(f"{self.config_prefix}_PASSWORD")
        if self.verify is None:
            self.verify = app.config.get(f"{self.config_prefix}_VERIFY")
        if self.g_session_key is None:
            self.g_session_key = app.config.get(f"{self.config_prefix}_G_SESSION_KEY")

    def create_session(self):
        session = requests.Session()
        if self.username and self.password:
            session.auth = HTTPBasicAuth(self.username, self.password)
        if self.verify is not None:
            session.verify = self.verify
        return session

    def request(self, method, path, session=None, **kwargs):
        url = self.base_url + path
        if session:
            cur_session = session
        elif self.g_session_key:
            cur_session = getattr(g, self.g_session_key, None)

        if not cur_session:
            cur_session = self.create_session()
        return cur_session.request(method, url, **kwargs)

    def get(self, path, **kwargs):
        return self.request("GET", path, **kwargs)

    def options(self, path, **kwargs):
        return self.request("OPTIONS", path, **kwargs)

    def head(self, path, **kwargs):
        return self.request("HEAD", path, **kwargs)

    def post(self, path, **kwargs):
        return self.request("POST", path, **kwargs)

    def put(self, path, **kwargs):
        return self.request("PUT", path, **kwargs)

    def patch(self, path, **kwargs):
        return self.request("PATCH", path, **kwargs)

    def delete(self, path, **kwargs):
        return self.request("DELETE", path, **kwargs)
