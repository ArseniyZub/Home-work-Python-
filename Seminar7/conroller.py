import operation
import view
import log

def button_click():
    oper = view.inp_mod()

    if oper.lower() == 'экспорт':
        elements = view.inp_export()
        operation.f_export(elements)
        log.log_cash()
        view.view_export()
    elif oper.lower() == 'импорт':
        surname = view.inp_import()
        result = operation.f_import(surname)
        if isinstance(result, str):
            view.view_import_no()
        else:
            view.view_import(result)
    else:
        view.view_exception()