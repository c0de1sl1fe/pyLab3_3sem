import os
import shutil


def create_dir(path: str) -> str:
    '''this function create 'dataset' directory
     in path gived by user
     and return path of new_dataset dir'''
    if not os.path.isdir(os.path.join(path, 'dataset')):
        os.mkdir(os.path.join(path, 'dataset'))
    return os.path.join(path, 'dataset')


def copy_dataset(class_name_copy: str, dst: str) -> None:
    '''copy all files in class_name_copy directory in data set to dst'''
    for item in os.listdir(os.path.join('dataset', class_name_copy)):
        if ".jpg" in item:
            s = os.path.join(os.path.join('dataset', class_name_copy), item)
            d = os.path.join(dst, f'{class_name_copy}_{item}')
            shutil.copy2(s, d)


def iterator2(class_name: str, path: str) -> str:
    '''Just interater for direcrory'''
    names = os.listdir(path)
    for i in names:
        if not class_name in i or not ".jpg" in i:
            names.remove(i)
    for i in range(len(names)):
        yield (names[i])
    return None


class Iterator2_img:
    def __init__(self, class_name: str, path: str):
        self.names = os.listdir(path)
        for i in self.names:
            if not class_name in i or not ".jpg" in i:
                self.names.remove(i)
        self.limit = len(self.names)
        self.counter = 0

    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            return self.names[self.counter - 1]
        else:
            raise StopIteration


def run_2(new_path_dir, name_class):
    '''main function, that toggle all realWorking functions'''
    new_dataset_path = create_dir(new_path_dir)
    copy_dataset(name_class, new_dataset_path)
