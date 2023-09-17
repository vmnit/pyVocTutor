from VocTutorEngineWithCLI import VocTutorEngineWithCLI


# from VocTutorEngineWithWindow import VocTutorEngineWithWindow


class VocTutor:
    def __init__(self, root_dir):
        self.vocTutorEngine = VocTutorEngineWithCLI(root_dir)

    def run(self):
        self.vocTutorEngine.run()
        #self.vocTutor.getDataFile()
