import csv
import os

from exceptions.file_write_exception import FileWriteException

class Writer:
    first_call = True

    def save_data(self, header, data, location):
        """
        Write data to a CSV  file.

        Args:
            header: Column names written as first row
            data: Scraped records to be written
            location: Path to the output CSV file
        """
        try:
            if self.first_call:
                self.first_call = False

                folder = os.path.dirname(location)

                for filename in os.listdir(folder):
                    filepath = os.path.join(folder, filename)

                    if os.path.isfile(filepath):
                        os.remove(filepath)
                
            file_exists = os.path.exists(location)

            with open(location, mode='a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)

                if not file_exists:
                    writer.writerow(header)

                writer.writerows(data)
        except OSError as e:
            raise FileWriteException('Failed to write to location. {}'.format(e))
