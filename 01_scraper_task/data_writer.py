import csv
import os

from exceptions.file_write_exception import FileWriteException

class Writer:
    def save_data(self, header, data, location):
        """
        Write data to a CSV  file.

        Args:
            header: Column names written as first row
            data: Scraped records to be written
            location: Path to the output CSV file
        """
        try:
            file_exists = os.path.exists(location)

            mode = 'a' if file_exists else mode = 'w'

            with open(location, mode=mode, newline='', encoding='utf-8') as file:
                writer = csv.writer(file)

                if not file_exists:
                    writer.writerow(header)

                writer.writerows(data)
        except OSError:
            raise FileWriteException('Failed to write to location')
