import numpy
import os
import urllib.parse
from datetime import datetime

class SimpleMethod:
    """
    TBD
    """
    def parse_binary(self, filename: str):
        with open(filename, mode = "rb") as logline:
            # line 1 is version info in a cloudfront log
            next(logline)
            # line two is headers with a prefix
            header = next(logline)

            fields = [
                name.decode("utf8")
                for name in header.replace(b"#Fields:", b"").split()
            ]



        print(fields)

        pass

    def parse(self, filename: str):
        with open(filename) as loglines:
            # line 1 is version info in a cloudfront log
            next(loglines)
            # line two is headers with a prefix
            header = next(loglines)

            fields = header.replace("#Fields:", "").split()

            for line in loglines:
                values = line.strip().split("\t")

                # a dictionary of the row of each value named for headers
                log_data = dict(zip(fields, values))

                # ensure we have a single datetime field, not separate dates and times
                log_data["date"] = str(datetime.strptime(
                    log_data.pop("date") + log_data.pop("time"),
                    "%Y-%m-%d%H:%M:%S"
                ))

                # return this row
                yield log_data


    def display(self, log):
        """_summary_

        Args:
            log (_type_): _description_

            will do some calculations and return a summary dict
        """
        pass

    def dicttest(self):
        dictionarytest = {
            'adate': datetime.now(),
            'astring': 'yeahboiii',
            'aninteger': 123,
            'afloat': 1.456
        }
        dictionarytest["anotherint"] = 1234
        return dictionarytest
