import csv  # module for precessing comma seperated files


def read_ints_csv(filename: str) -> bool:
    """The file `filename` is guaranteed to be a CSV file  (comma seperated
    variables) with variable length records and integer valued fields.

    Every record should comply with the constraints that:
    * Every record has either zero fields or at least two fields
    * The value in the last field of a record must equal the sum of all the
      preceding fields in that record

    Open the file, read it, and return `True` if it complies with these
    constraints and `False` otherwise."""

    with open(filename) as csvfile:
        # read file as a CSV file
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            len_row = len(row)
            # record cannot have one field
            if len_row == 1:
                return False
            # all the fields are text so cast to integer
            row = list(map(int, row))
            # LAST field must equal sum of all other fields
            if not row[len_row - 1] == sum(row[:-1]):
                return False
    # file read and all tests passed!
    return True
