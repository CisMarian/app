import json


class Database:
    def __init__(self, name_space):
        self.name_space = name_space
        self.files = {}
        self.create()

    def create(self):
        if self.name_space in self.files:
            return False
        else:
            self.files[self.name_space] = []
            self._save_file(self.name_space)
            return True

    def add(self, name_space, fields):
        if name_space in fields:
<<<<<<< HEAD
            return -1
=======
            raise OSError("Namespace already exist!")
>>>>>>> 0ccbc45 (add jsondb extension)

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

<<<<<<< HEAD
    def get_by_id_1(self, name_space):
=======
    def get_by_id(self, name_space, record_id):
>>>>>>> 0ccbc45 (add jsondb extension)
        if name_space not in self.files:
            return []

        for record in self.files[name_space]:
<<<<<<< HEAD
            if record['id'] == 1:
=======
            if record['id'] == record_id:
>>>>>>> 0ccbc45 (add jsondb extension)
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
