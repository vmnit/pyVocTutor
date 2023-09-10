from VocTutorEngineWithCLI import VocTutorEngineWithCLI


# from VocTutorEngineWithWindow import VocTutorEngineWithWindow


class VocTutor:
    def __init__(self, root_dir):
        self.vocTutor = VocTutorEngineWithCLI(root_dir)

    def run(self):
        self.vocTutor.run()
        #self.vocTutor.getDataFile()
