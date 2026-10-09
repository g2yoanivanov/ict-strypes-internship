from abc import ABC, abstractmethod

import os


class Writer(ABC):
    """
    Abstract base class for all the different format writes.
    """

    @abstractmethod
    def save_data(self, header, data, location, first_call):
        """
        Save data to a chosen location in a specific format.
        """
        if first_call:
            first_call = False

            folder = os.path.dirname(location)

            os.makedirs(folder, exist_ok=True)

            for filename in os.listdir(folder):
                filepath = os.path.join(folder, filename)

                if os.path.isfile(filepath):
                    os.remove(filepath)
