"""
SRP single responsability principle advocates when defining a class to provide functionality,
that class should have only one reason to exist and should be responsible for only one aspect
of the functionality, it promotes the idea that each class should have one job/responsability
"""

# SRP teaches us to separate things

class Report:
    def __init__(self, content: str):
        self.content: str = content

    def generate(self) -> None:
        print(f"Report content: {self.content}")

class ReportSaver:
    def __init__(self, report: Report):
        self.report: Report = report

    def save_to_file(self, filename: str):
        with open(filename, 'w', encoding='utf-8') as f: # by using the utf-8 we avoid file corruption
            f.write(self.report.content)                 # if unicode characters are present in the parsing

if __name__ == "__main__":
    report_content = "This is a text to be saved as report"
    report = Report(report_content)
    report.generate() # if you want to see it stdout

    report_saver = ReportSaver(report)
    # report_saver.save_to_file("report.txt")
