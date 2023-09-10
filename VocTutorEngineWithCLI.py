import sys

from VocTutorEngine import VocTutorEngine


class VocTutorEngineWithCLI(VocTutorEngine):
    def __init__(self, root_dir):
        super().__init__(root_dir)
        self.initializeMenu()

    def initializeMenu(self):
        print(self.title)
        self.create_user_menu()
        self.create_vocab_menu()

        if not self.data_file_exists():
            trials = self.get_num_trials()
            self.set_data_file(num_trials=trials)
        else:
            self.set_data_file()
        self.initialize_data()

    def create_user_menu(self):
        users_list = self.get_users()
        self.user = self.create_menu(users_list)
        print(f"\nYou have entered user: {self.user}")

    def create_vocab_menu(self):
        file_list = self.get_file_options()
        self.vocab_file = self.create_menu(file_list)
        print(f"\nYou have entered vocabulary file: {self.vocab_file}")

    def create_num_trials_menu(self):
        while True:
            try:
                num_trials = int(input("\nEnter num of trials (1-10) for each word: "))
            except ValueError:
                print("Wrong input. It should be integer. Try again")
                continue

            if 0 > num_trials >= 10:
                print(f"Wrong input {num_trials}. It should be between 1-10. Try again")
                continue

            return num_trials

    def create_menu(self, option_list):
        while True:
            if len(option_list):
                print("Select option from the given list: ")

            total_cnt = 1
            for user in option_list:
                print(f"{total_cnt}. {user}")
                total_cnt += 1

            print("\nPress '0' to add new entry or 'q' to quit the menu .")

            user_option = input("Enter your option: ")
            if user_option == 'q':
                sys.exit(0)

            try:
                opt = int(user_option)
            except ValueError:
                print(f"Wrong input {user_option}. Try again.\n\n")
                continue

            if 0 > opt >= total_cnt:
                print(f"Wrong input {user_option}. Try again.\n\n")
                continue

            if 1 <= opt < total_cnt:
                selected_option = option_list[opt - 1]
                return selected_option

            self.is_num_trials_required = True
            return input("Enter new entry: ")

    def create_run_menu(self, word_idx, meaning_indices):
        while True:
            print(f"Meaning of word: {self.data.iloc[word_idx]['Word']}\n")

            total_cnt = 0
            for meaning_idx in meaning_indices:
                #print(meaning_idx)
                print(f"{total_cnt + 1}. {self.data.iloc[meaning_idx]['Meaning']}")
                total_cnt += 1

            print("\nPress 'q' to quit the game.")

            user_option = input("Enter your option: ")
            if user_option == 'q':
                return True

            try:
                opt = int(user_option)
            except ValueError:
                print(f"Wrong input {user_option}. Try again.\n\n")
                continue

            if 0 >= opt > len(meaning_indices):
                print(f"Wrong input {user_option}. Try again.\n\n")
                continue

            #print(len(meaning_indices), opt-1, meaning_indices[opt-1], meaning_indices)
            if self.check_answer(word_idx, meaning_indices[opt-1]):
                trials_remaining = self.get_num_trials(word_idx)
                print(f"Your answer is CORRECT. Number of trials reduced to: {trials_remaining}")
            else:
                trials_remaining = self.get_num_trials(word_idx)
                print(f"Your answer is WRONG. You will get following number of chances: {trials_remaining}")
            return False

    def run(self):
        while True:
            idx = self.get_random_word_index()
            #print(idx)
            option_indices = self.get_random_options(idx)
            if self.create_run_menu(idx, list(option_indices)):
                break
