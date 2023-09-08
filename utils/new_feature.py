import json
import func

with open('operations.json') as f:
    list_operat = json.load(f)
sort_operations = func.sort_operat(list_operat)
func.print_info(sort_operations)
