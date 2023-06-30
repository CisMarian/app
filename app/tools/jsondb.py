import json


class Database:
    def __init__(self, name_space):
        self.name_space = name_space
        self.files = {}
        self._load_file()

    def create(self):
        self.files[self.name_space] = []
        self._save_file()
        return True

    def add(self, fields):
        records = self.files[self.name_space]
        if len(records) == 0:
            new_id = 1
        else:
            new_id = records[-1]['id'] + 1

        fields['id'] = new_id
        records.append(fields)
        self._save_file()
        return new_id

    def delete(self, record_id):
        records = self.files[self.name_space]
        for record in records:
            if record['id'] == record_id:
                records.remove(record)
                self._save_file()
                return True
        return False

    def get_all(self):
        return self.files[self.name_space]

    def get_by_id(self, record_id):
        for record in self.files[self.name_space]:
            if record['id'] == record_id:
                return [record]

        return []

    def update(self, fields):
        records = self.files[self.name_space]
        for record in records:
            if record['id'] == fields['id']:
                record.update(fields)
                self._save_file()
                return True

        return False

    def _load_file(self):
        filename = self._get_file_name()
        try:
            with open(filename, 'r') as file:
                self.files[self.name_space] = json.load(file)
        except FileNotFoundError:
            self.files[self.name_space] = []

    def _save_file(self):
        filename = self._get_file_name(self.name_space)
        try:
            with open(filename, 'w') as file:
                json.dump(self.files[self.name_space], file, indent=2)
        except OSError:
            raise OSError("Plik {} już istnieje.".format(filename))

    def _get_file_name(self):
        return '.'.join([self.name_space, 'json'])
