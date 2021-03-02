import json


class Person(object):
    def __init__(self, first_name, last_name, date_of_birth):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth

    def toJSON(self):
        with open("temp.json", "w") as f:
            return json.dump(
                self, f, default=lambda o: o.__dict__, sort_keys=True, indent=4
            )


"""
measurements (list_of_dicts):

json_writer -> 36.4 ms ± 1.93 ms per loop
xml_writer -> 19.8 ms ± 112 µs per loop
pickle_writer -> 2.06 ms ± 29.9 µs per loop

read_json -> 3.34 ms ± 22.2 µs per loop
read_xml -> 21.2 ms ± 2.84 µs per loop
read_pickle -> 1.96 ms ± 116 µs per loop

measurements (dict_of_lists):

json_writer -> 22.3 ms ± 118 µs per loop
xml_writer -> 10.8 ms ± 112 µs per loop
pickle_writer -> 1.93 ms ± 132 µs per loop

read_json -> 3.64 ms ± 424 µs per loo
read_xml -> 20.8 ms ± 2.84 µs per loop
read_pickle -> 1.7 ms ± 87.8 µs per loop
"""
