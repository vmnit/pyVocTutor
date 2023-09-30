import sys

from VocTutorEngine import VocTutorEngine


# def get_char(prompt):
#     import readchar
#     print(prompt)
#     key = readchar.readkey()
#     print(key)
#     return key


class VocTutorEngineWithCLI(VocTutorEngine):
    def __init__(self, root_dir):
        super().__init__(root_dir)

    def show_title(self):
        print("*" * (len(self.title) + 4))
        print(f"* {self.title} *")
        print("*" * (len(self.title) + 4))
        print("")

    def show_user_menu(self):
        self.show_title()
        users_list = self.get_users()
        ret_val, self.user = self.show_menu("user", users_list)
        if not ret_val:
            return False

        print(f"\nYou have entered user: {self.user}")
        return True

    def show_datafile_menu(self):
        self.show_title()
        file_list = self.get_file_options()
        ret_val, self.vocab_file = self.show_menu("vocabulary file", file_list)
        if not ret_val:
            return False

        print(f"\nThe entered vocabulary file: {self.vocab_file} will be copied over ")
        return True

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

    def show_menu(self, type, option_list):
        while True:
            if len(option_list):
                print(f"Select {type} from the given list: ")

            total_cnt = 1
            for user in option_list:
                print(f"{total_cnt}. {user}")
                total_cnt += 1

            print(f"\nPress 'n' to add new {type} or 'e' to exit this menu .")

            user_option = input("Enter your option: ")
            if user_option == 'e':
                return False, ''

            if user_option == 'n':
                self.is_num_trials_required = True
                return True, input(f"Enter new {type}: ")

            try:
                opt = int(user_option)
            except ValueError:
                print(f"Wrong input {user_option}. Try again.\n\n")
                continue

            if 1 > opt or opt >= total_cnt:
                print(f"Wrong input {user_option}. Try again.\n\n")
                continue

            selected_option = option_list[opt - 1]
            return True, selected_option


    def show_question_menu(self, word_idx, meaning_indices):
        while True:
            print()
            print("*" * 50)
            print(f"Meaning of word: {self.data.iloc[word_idx]['Word']}\n")

            total_cnt = 0
            for meaning_idx in meaning_indices:
                #print(meaning_idx)
                print(f"{total_cnt + 1}. {self.data.iloc[meaning_idx]['Meaning']}")
                total_cnt += 1

            print("\nPress 'q' to exit this game and return to previous menu.")

            user_option = input("Enter your option: ")
            if user_option == 'q':
                return False

            try:
                opt = int(user_option)
            except ValueError:
                print(f"Wrong input {user_option}. Try again.\n\n")
                continue

            if 0 >= opt or opt > len(meaning_indices):
                print(f"Wrong input {user_option}. Try again.\n\n")
                continue

            #print(len(meaning_indices), opt-1, meaning_indices[opt-1], meaning_indices)
            if self.check_answer(word_idx, meaning_indices[opt-1]):
                trials_remaining = self.get_num_trials(word_idx)
                print(f"Your answer is CORRECT. Number of trials reduced to: {trials_remaining}")
            else:
                trials_remaining = self.get_num_trials(word_idx)
                print(f"Your answer is WRONG. You will get following number of chances: {trials_remaining}")
                print(f"Correct answer is: {self.get_answer(word_idx)}")

            print()
            # TODO: Need to implement get_char to stop for users' keystroke to proceed.
            #  Right now, facing hanging issue.
            #  For now, using input() which will require <Enter> key to be pressed.
            # char = get_char("Press any key to continue...")
            input("Press any key to continue... ")
            return True


