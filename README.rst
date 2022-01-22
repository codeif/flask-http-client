HTTP client extension for Flask.
===========================================

对requests库的包装，在flask配置文件中配置base_url, auth, 转发user-agent等。第一次访问网址生成全局的session, 本次request结束后， 关闭此session。


安装
------

.. code-block:: sh

    pip install flask-http-client

使用
------


First init::

    from flask_http_client import HTTPClient
    http_client = HTTPClient()
    http_client.init_app(app)

API
----

和requests的API一致，需要注意的是 url = base_url + path，所以base_url和path需要自己做好处理。

.. code-block::

    params = {}
    resp = http_client.request('GET', '/users/', params=params)
    resp = http_client.get('/users', params=params)


配置项
------

可以在构造方法修改配置前缀，默认为 HTTP_CLIENT

.. code-block:: py

    http_client = HttpClient(config_prefix='YOUR_CONFIG_PREFIX')


=====================   ================================================
配置项                      说明
=====================   ================================================
HTTP_CLIENT_BASE_URL    api的url_prefix
HTTP_CLIENT_AUTH        requests中的auth参数
=====================   ================================================
