
from utils.helpers import generate_id
from utils.storage import load_data, save_data
class UserService:

    # REGISTER USER
    def register_user(
        self,
        username,
        password,
        role
    ):

        data = load_data()

        users = data.setdefault(
            "users",
            []
        )

        # CHECK DUPLICATE
        for user in users:

            if user["username"] == username:

                print(
                    "Username already exists"
                )

                return False

        # CREATE USER
        new_user = {
            "id": generate_id(users, "US"),
            "username": username,
            "password": password,
            "role": role
        }

        users.append(new_user)

        save_data(data)

        print(
            "User registered successfully"
        )

        return True

    # VIEW USERS
    def get_users(self):

        data = load_data()

        return data.get(
            "users",
            []
        )

    # FIND USER
    def find_user(
        self,
        username
    ):

        data = load_data()

        for user in data.get(
            "users",
            []
        ):

            if (
                user["username"].lower()
                ==
                username.lower()
            ):

                return user

        return None

    # UPDATE USER
    def update_user(
        self,
        username,
        new_password,
        new_role
    ):

        data = load_data()

        for user in data.get(
            "users",
            []
        ):

            if (
                user["username"].lower()
                ==
                username.lower()
            ):

                user["password"] = new_password
                user["role"] = new_role

                save_data(data)

                return True

        return False

    # DELETE USER
    def delete_user(
        self,
        username
    ):

        data = load_data()

        users = data.get(
            "users",
            []
        )

        for user in users:

            # PREVENT ADMIN DELETE
            if (
                user["username"].lower()
                ==
                username.lower()
            ):

                if user["role"] == "admin":

                    print(
                        "Admin cannot be deleted"
                    )

                    return False

                users.remove(user)

                save_data(data)

                return True

        return False

