import whisper


class run_model:
    def __init__(self):
        self.model = whisper.load_model("small", download_root=r"model")

    def run(self, audio="自录的原神启动.wav"):
        result = self.model.transcribe(audio, language="zh")
        return result["text"]

if __name__ == '__main__':
    model = run_model()
    model.run()