import time
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()

        print(f"execution time: {end-start:.5f} seconds.")
        return result
    return wrapper 

# making class 
class Datasetprocessor:
#constractor
    def __init__(self, filename):
        self.filename = filename
#genarator read file
    def read_scores(self):
        with open(self.filename) as file:
            for line in file:
                yield int(line.strip())

#comperhension  return the numbers are passed
    def passed_scores(self):
        return [score for score in self.read_scores() if score >= 60]

    @staticmethod
    def average(scores):
        return sum(scores) / len(scores)

    @classmethod
    def load(cls, filename):
        return cls(filename)


    @timer
    def process(self):
        passed = self.passed_scores()
        avg = self.average(passed)
        print("passed Scores:", passed)
        print("Average:", avg)



    def exellent(self):
        return [score for score in self.read_scores()
             if score >= 50]


processor = Datasetprocessor.load("week2/day7/dataset.txt")
processor.process()
print(processor.exellent())
status = ["pass" if score >= 50 else "fail"
          for score in processor.read_scores()]
print(status)
scores = list(processor.read_scores())
print(max(scores))
print(min(scores))
new_state = ["Exellent Student" if score >= 40 else "Failed"
             for score in processor.read_scores()]
print(new_state)




























