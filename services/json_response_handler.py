from flask import jsonify


class JsonResponseHandler:
    def send_response(self, data):
        users_list = []
        for user in data:
            users_list.append({'id': user.id, 'username': user.username})
        return jsonify(users_list)