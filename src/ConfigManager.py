import configparser
import os


class ConfigManager:
    def __init__(self, config_file_path):
        self.config = configparser.ConfigParser(delimiters=('='))
        self.config_file_path = config_file_path
        self.load_config()

    def load_config(self):
        if not self.config.read(self.config_file_path):
            print(f"Config file '{self.config_file_path}' not found. Creating a new one.")
            self.save_config()

    def save_config(self):
        os.makedirs(os.path.dirname(self.config_file_path), exist_ok=True)
        with open(self.config_file_path, 'w') as configfile:
            self.config.write(configfile)

    def get_value(self, section, key):
        try:
            return self.config.get(section, key)
        except configparser.NoSectionError:
            print(f"Section '{section}' not found in config file.")
            return None
        except configparser.NoOptionError:
            # print(f"Key '{key}' not found in section '{section}' of the config file.")
            return None

    def set_value(self, section, key, value):
        if not self.config.has_section(section):
            self.config.add_section(section)
        self.config.set(section, key, value)
        self.save_config()

    def get_sections(self):
        return self.config.sections()

    def get_keys_in_section(self, section):
        if self.config.has_section(section):
            # print(self.config.options(section))
            return self.config.options(section)
        else:
            print(f"Section {section} not found in config file")
            return []
