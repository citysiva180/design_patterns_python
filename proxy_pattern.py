# The Proxy Design Pattern is a structural design pattern that provides a surrogate
# or placeholder for another object to control access to it. It is often used when
# you want to add an extra layer of control or functionality to an object without
# modifying its core behavior. One common use case for the Proxy Pattern is in the
# implementation of internet proxies.

# Example: Imagine you're developing an internet proxy server that sits between a client
# and a remote server. The proxy can control access to the internet, apply access control
# rules, log requests, or even cache responses. The proxy, in this case, acts as a surrogate
# for the remote server, providing additional functionalities.


# Internet base class
class Internet:
    def connect(self, url):
        pass

# Real Internet Concrete Class


class RealInternet(Internet):
    def connect(self, url):
        print(f"connecting to {url}")

# InternetProxy Class for adding Object


class InternetProxy(Internet):
    def __init__(self):
        self.internet = RealInternet()

    def connect(self, url):
        if self.is_access_allowed(url):
            self.internet.connect(url)
        else:
            print("Access Denied")

    def is_access_allowed(self, url):
        white_listed_ips = [
            "123.345.343.4",
            "123.345.343.5",
            "123.345.343.6",
            "123.345.343.7",
            "123.345.343.8"
        ]

        if url in white_listed_ips:
            return True
        else:
            return False
