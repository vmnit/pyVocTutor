import os
import random
import sys
from abc import ABC, abstractmethod
from datetime import datetime

from ConfigManager import ConfigManager
import pandas as pd
import numpy as np
import icecream as ic


class VocTutorEngine(ABC):
    def __init__(self, root_dir):
        self.indices = None
        self.data = None
        self._user_dir = None
        self.config_manager = ConfigManager(os.path.join(root_dir, "pyVocTutor.ini"))
        self._user = None
        self.vocab_file = None
        self.data_file = None
        self.root_dir = root_dir
        self.is_num_trials_required = False

    @property
    def title(self):
        return "PyVocTutor: Best Vocabulary tutor"

    def get_users(self):
        return self.config_manager.get_sections()

    def get_file_options(self):
        return self.config_manager.get_keys_in_section(self.user)

    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, user):
        self._user = user

    @property
    def user_dir(self):
        user_dir = os.path.join(self.root_dir, self.user)
        try:
            if not os.path.exists(user_dir):
                os.makedirs(user_dir, exist_ok=True)
        except OSError:
            sys.exit(f"Unable to create directory: {user_dir}")

        self.user_dir = user_dir
        return self._user_dir

    @user_dir.setter
    def user_dir(self, value):
        self._user_dir = value

    def data_file_exists(self):
        data_file = self.config_manager.get_value(self.user, self.vocab_file)
        if not data_file:
            return False

        return os.path.exists(data_file)

    def set_data_file(self, num_trials=-1):
        if not self.data_file_exists():
            if num_trials < 0:
                raise ValueError("Negative number of trials not supported.")

            data_file = self.create_data_file(num_trials)
            self.config_manager.set_value(self.user, self.vocab_file, data_file)

        self.data_file = self.config_manager.get_value(self.user, self.vocab_file)
        return self.data_file

    def update_data_file(self):
        self.data.to_csv(self.data_file, index=None)

    def create_data_file(self, num_trials):
        data_file = f"data_{datetime.today().strftime('%Y_%m_%d_%H%M%S')}.dat"
        data_file_path = os.path.join(self.user_dir, data_file)
        df = pd.read_csv(self.vocab_file, names=['Word', 'Meaning'], header=None)
        df["Trials"] = num_trials
        df.to_csv(data_file_path, index=None)
        return data_file_path

    def initialize_data(self):
        self.data = pd.read_csv(self.data_file)

    @abstractmethod
    def create_user_menu(self):
        pass

    @abstractmethod
    def create_vocab_menu(self):
        pass

    @abstractmethod
    def create_run_menu(self):
        pass

    @abstractmethod
    def create_num_trials_menu(self):
        pass

    def get_random_word_index(self):
        list_indices = self.data[self.data.Trials > 0].index.tolist()
        #print(list_indices)
        return random.choice(list_indices)

    def get_random_index(self):
        if not self.indices:
            self.indices = self.data.index.values.tolist()
        return random.randint(min(self.indices), max(self.indices))

    def check_answer(self, idx, meaning_idx):

        if idx == meaning_idx:
            self.data.at[idx, "Trials"] -= 1

            if self.data.iloc[idx]["Trials"] < 0:
                raise ValueError(f"Number of trials gone to negative for word index: {idx}")

            self.update_data_file()
            return True
        return False

    def get_answer(self, idx):
        return self.data.at[idx, "Meaning"]

    def get_random_options(self, idx):
        indices = set()
        indices.add(idx)
        #print(indices)

        data_len = len(self.data)
        while len(indices) < min(6, data_len):
            new_idx = self.get_random_index()
            #print(new_idx)
            indices.add(new_idx)

        #print(indices)
        return indices

    def get_num_trials(self, word_idx):
        return self.data.iloc[word_idx]['Trials']

    def run(self):
        while True:
            idx = self.get_random_word_index()
            #print(idx)
            option_indices = self.get_random_options(idx)
            if not self.create_run_menu(idx, list(option_indices)):
                break
