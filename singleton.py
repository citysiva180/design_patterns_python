def singleton(cls):

    instances = {}  # This dictionary stores all instances

    def get_instances(*args, **kwargs):

        # This function checks if an instance exists
        # if the function exisits, then it will return that instance
        # else it will create a new instance

        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instances

# Here a class is being created using decorator


@singleton
class DatabaseConnection:

    # This database class initializes an database connection object
    # At first the instance object will say that the connection is not done
    # After which it would connect

    def __init__(self, db_url):
        self.db_url = db_url
        self.connected = False

    def connect(self):
        if not self.connected:
            print(f"Connecting to {self.db_url}")
            self.connected = True

    def disconnect(self):
        if self.connected:
            print(f"Disconnecting from {self.db_url}")
            self.connected = False


# Creating Multiple connections and checking out!
db_connection_1 = DatabaseConnection("oracle.com")
db_connection_2 = DatabaseConnection("mysql.com")


print(db_connection_1 is db_connection_2)

db_connection_1.connect()
db_connection_1.disconnect()


db_connection_2.connect()
db_connection_2.disconnect()
