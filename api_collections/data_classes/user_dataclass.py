import random

from faker import Faker

fake = Faker()


class UserData:
    def __init__(self, **kwargs):
        self.__dict__.update(**kwargs)

    def get_dict(self):
        return self.__dict__

    @staticmethod
    def get_fake_user_payload():
        return {
            "firstName": fake.name(),
            "lastName": fake.last_name(),
            "email": fake.email()
        }

    @staticmethod
    def get_fake_user_without_email():
        return {
            "firstName": fake.name(),
            "lastName": fake.last_name()
        }

    @staticmethod
    def get_fake_post_payload():
        return {
            "text": fake.sentence(5),
            "likes": random.randint(1, 50)
        }

