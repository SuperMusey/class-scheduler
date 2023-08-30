import pickle
import os

class PickleHandler:
    def __init__(self):
        self.list_pickle_data = {}

    def open_named_pickles(self, list_pickles):
        '''Put in name of pickle files as list. Name is from start to _data'''
        for name in list_pickles:
            print("Opening -- ",name)
            with open(os.path.join('Data', name + '_data.pkl'), "rb") as pickle_file:
                data = pickle.load(pickle_file)
                self.list_pickle_data[name] = data
        
    def view_last_n_entries(self, filename, n):
        data = self.list_pickle_data[filename]
        print("Last ",n," keys of",filename," :")
        _keys_ = list(data.keys())[-n:]
        for idx, key in enumerate(_keys_):
            print("Insertion at ",idx," : ",key)
            print("With data -> ",data[key])

    def view_first_n_entries(self, filename, n):
        data = self.list_pickle_data[filename]
        print("First ",n," keys of",filename," :")
        _keys_ = list(data.keys())[:n]
        for idx, key in enumerate(_keys_):
            print("Insertion at ",idx," : ",key)
            print("With data -> ",data[key])
    
    def delete_keys(self, filename, keys):
        print("Deleting from : ",filename, "keys: ",keys)
        data = self.list_pickle_data[filename]
        for key in keys:
            if key in data:
                print("Deleted ",key)
                del data[key]
            else:
                print(key," not found!")
    
    def append_data(self, filenames, picklename):
        '''filenames -> List of filesnames to append to end of each other
        if list [a,b,c] appends b to a and c to b and stores in picklename'''
        to_combine_data = []
        for file in filenames:
            to_combine_data.append(self.list_pickle_data[file])

        combined_dict = {}
        for d in to_combine_data:
            for key, value in d.items():
                if key in combined_dict:
                    combined_dict[key].append(value)
                else:
                    combined_dict[key] = value

        with open(os.path.join('Data', picklename + '_data.pkl'), "wb") as pickle_file:
            pickle.dump(combined_dict, pickle_file)
        print("Saved to ",picklename)




