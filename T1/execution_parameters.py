from functions import *
from utils import get_interval_for_function

processes_number = 10  # Number of threads used
algorithm = "HC"  # "HC" or "SA"
mode = "worst"  # Only for "HC" algorithm: "first", "best" or "worst"
function = schwefel
dimension = 30
interval = get_interval_for_function(function)

exec_precision = 5