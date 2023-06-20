import json


class Database:
    def __init__(self):
        self.files = {}

    def use(self, name_space):
        self.name_space = name_space

    def create(self):
        if self.name_space in self.files:
            return False
        else:
            self.files[self.name_space] = []
            self._save_file(self.name_space)
            return True

    def add(self, name_space, fields):
        if name_space in fields:
            raise OSError("Namespace already exist!")

        records = self.files[name_space]
        if len(records) == 0:
            new_id = 1
        else:
            new_id = records[-1]['id'] + 1

        fields['id'] = new_id
        records.append(fields)
        self._save_file(name_space)
        return new_id

    def delete(self, name_space, record_id):
        if name_space in self.files:
            return False

        records = self.files(name_space)
        for record in records:
            if record['id'] == record_id:
                record.remove(record)
                self._save_file(name_space)
                return True
        False

    def get_all(self, name_space):
        if name_space not in self.files:
            return []

        return self.files[name_space]

    def get_by_id(self, name_space, record_id):
        if name_space not in self.files:
            return []

        for record in self.files[name_space]:
            if record['id'] == record_id:
                return [record]

        return []

    def update(self, name_space, fields):
        if name_space not in self.files:
            return False

        records = self.files[name_space]
        for record in records:
            if record['id'] == fields['id']:
                record.update(fields)
                self._save_file(name_space)
                return True

        return False

    def _save_file(self, name_space):
        if name_space in self.files:
            filename = f'{name_space}.json'
            with open(filename, 'w') as file:
                json.dump(self.files[name_space], file, indent=2)
