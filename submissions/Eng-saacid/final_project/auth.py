from utils.storage import load_data


class Auth:

    def login(self, username, password):

        data = load_data()

        for user in data.get("users", []):

            if user["username"] == username and user["password"] == password:
                return user

        return None

