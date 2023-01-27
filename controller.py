import view
import export
import sorting

def start():
    text_operation = view.select_operation()

    if text_operation == 1:
        view.init_information()
    elif text_operation == 2:
        export.output_all_information()
    elif text_operation == 3:
        export.output_names()
    elif text_operation == 4:
        sorting.name_sorting()
    elif text_operation == 5:
        sorting.id_sorting()
    else:
        print('Введён неверный номер операции')
        
