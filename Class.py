class Platform:
    def __init__(self):
        self.__accounts = []  # List to store accounts

    def add_account(self, account):
        self.__accounts.append(account)

    def search_account(self, email):
        for account in self.__accounts:
            if account.email == email:
                return account
        return None


class Account:
    def __init__(self, email, password, name, username):
        self.__email = email
        self.__password = password
        self.__name = name
        self.__username = username
        self.__tel = None  # Phone number is not set initially
        self.__location = Location()
        self.__cart = []
        self.__course = []
        self.__order_history = []

    def edit_data(self, email, name, tel, location):
        self.__email = email
        self.__name = name
        self.__tel = tel
        self.__location.edit_location(location)

    @property
    def email(self):
        return self.__email

    @property
    def name(self):
        return self.__name

    @property
    def tel(self):
        return self.__tel

    @property
    def location(self):
        return self.__location


class Location:
    def __init__(self):
        self.__country = None
        self.__street_address = None
        self.__apt = None
        self.__suburb = None
        self.__city = None
        self.__province = None
        self.__postal_code = None

    def edit_location(self, location):
        self.__country = location[0]
        self.__street_address = location[1]
        self.__apt = location[2]
        self.__suburb = location[3]
        self.__city = location[4]
        self.__province = location[5]
        self.__postal_code = location[6]

    @property
    def country(self):
        return self.__country

    @property
    def street_address(self):
        return self.__street_address

    @property
    def apt(self):
        return self.__apt

    @property
    def suburb(self):
        return self.__suburb

    @property
    def city(self):
        return self.__city

    @property
    def province(self):
        return self.__province

    @property
    def postal_code(self):
        return self.__postal_code
