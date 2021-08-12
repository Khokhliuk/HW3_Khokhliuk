from contextlib import contextmanager
from openpyxl import Workbook


@contextmanager
def workbook_new(filepath):
    workbook = Workbook()
    try:
        yield workbook
    except:
        print("Something went wrong!")
    finally:
        workbook.save(filepath)


with workbook_new('ex_file.xlsx') as workbook:
    worksheet = workbook.active
    worksheet.cell(row=1, column=1, value="Hello world!")