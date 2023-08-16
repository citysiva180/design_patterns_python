from abc import ABC, abstractmethod


class Country:
    pass


class UnitedStates:
    pass


class India:
    pass


class Japan:
    pass


class CurrencyFactory(ABC):
    @abstractmethod
    def currency_factory(self, country) -> str:
        pass


class CountryCurrencies(CurrencyFactory):

    def currency_factory(self, country) -> str:

        if country is UnitedStates:
            return "USD"

        if country is India:
            return "INR"

        if country is Japan:
            return "JPY"


class VirtualCurrencies(CurrencyFactory):

    def currency_factory(self, country) -> str:

        if country is UnitedStates:
            return "BitCoin"

        if country is India:
            return "CryptoIndianCoin"

        if country is Japan:
            return "ShibaInu"


# In the above example we had sub-classes which we just created. However the instantiation and the
# behaviour of these classes were defined in the subclasses.
# This helps in modifying the class for plenty of different options

if __name__ == "__main__":

    c1 = CountryCurrencies()
    c2 = VirtualCurrencies()

    print(c1.currency_factory(UnitedStates))
    print(c1.currency_factory(India))
    print(c1.currency_factory(Japan))

    # On invoking the c1.currency_factory(unitedstates class) the program will first go to country_currencies
    # There it will note that currency_factory is being used. It goes to the currency factory template class
    # There it will see that there is a function and that function accepts the country name, which in this case is a
    # class name. But it will not do anything cause in both the UnitedStates class and Currency factory class
    # Hence the power will come to CountryCurrency class where the changes would be applied!

    print(c2.currency_factory(UnitedStates))
    print(c2.currency_factory(India))
    print(c2.currency_factory(Japan))
