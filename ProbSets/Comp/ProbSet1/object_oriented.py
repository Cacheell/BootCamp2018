class Backpack:
    """A Backpack object class. Has a name, color, and max_size and a list of contents.
    Attributes:
        name (str): the name of the backpack's owner.
        color (str): the color of the backpakself.
        max_size (int): the maximum length of the backpack's contents.
        contents (list): the contents of the backpack.
    """
    def __init__(self, name, color, max_size=5):           # This function is the constructor.
        """Set the name, color, max_size and initialize an empty list of contents.
        Parameters:
            name (str): the name of the backpack's owner
            color(str): the color of the Backpack
            max_size(int): the max length of the backpack's contents.   The
        default is 5.
        """
        self.name = name                # Initialize some attributes.
        self.color = color
        self.max_size = max_size
        self.contents = []

    def __eq__(self, other):
        """"""
        nameeq = self.name == other.name
        coloreq = self.color == other.color
        contentseq = len(self.contents) == len(other.contents)
        return (nameeq and coloreq and contenteq)

    def __str__(self):
        """"""
        print("Owner:\t", self.name, "\nColor:\t", self.color, "\nSize:\t",
              len(self.max_size), "\nContents:\t", self.contents)

    def put(self, item):
        """Add 'item' to the backpack's list of contents if the size of the
        contents is less than the maximum size"""
        if (len(self.contents) >= self.max_size):
            print("No Room!")
        else:
            self.contents.append(item)  # Use 'self.contents', not just 'contents'.
    def take(self, item):
        """Remove 'item' from the backpack's list of contents."""
        self.contents.remove(item)
    def dump(self):
        """Reset the contents of the backpack"""
        self.contents = []
        print("You dumped out your backpack!")


class Jetpack(Backpack):
        """A jetpack object class. Inherits from the Backpack class.
        A jetpack is smaller than a backpack and contains fuel.
        Attributes:
        name (str): the name of the jetpack's owner.
        color (str): the color of the jetpack.
        max_size (int): the maximum number of items that can fit inside.
        contents (list): the contents of the jetpack.
        fuel (int): the amount of fuel.
        """
    def __init__(self, name, color, max_size=2, fuel=10):
        """Use the Backpack constructor to initialize the name, color,
        and max_size attributes and adds fuel.  A jetpack only holds 2 items
        by default and 10 fuel by default.
        Parameters:
            name (str): the name of the jetpack's owner.
            color (str): the color of the jetpack.
            max_size (int): the maximum number of items that can fit inside.
            fuel (int): the amount of fuel the jetpack has.
        """
        self.fuel = fuel

    def fly(self, fuelamount):               #define a new method
        """Fly the jetpack.  This checks to see if the argument or the amount
        you want to fly is below or equal to the amount of fuel you have.  If
        so minus that amount off your fuel."""
        if fuelamount > self.fuel
            print("Not enough fuel!")
        else:
            self.fuel = self.fuel - fuelamount
    def dump(self):          #overide the put() method
        "dump out contents and fuel"
        self.contents = []
        self.fuel = 0
