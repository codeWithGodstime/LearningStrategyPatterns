import factory


class TestDataHelper():

    @classmethod
    def get_data(cls, type):
        return factory.build(dict, FACTORY_CLASS=type)