import flask
from dict2xml import dict2xml
from flask import render_template


class XmlResponseHandler:
    def send_response(self, data):
        users_list = []
        for user in data:
            users_list.append({'id': user.id, 'username': user.username})
        xml_str = f'<document>{dict2xml(users_list)}</document>'

        res = flask.Response(xml_str, 200)

        res.headers['Content-Type'] = 'application/xml'
        return res