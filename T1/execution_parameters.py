from functions import *
from utils import get_interval_for_function

processes_number = 10  # Number of threads used
algorithm = "HC"  # "HC" or "SA"
mode = "best"  # Only for "HC" algorithm: "first", "best" or "worst"
function = de_jongs
dimension = 5
interval = get_interval_for_function(function)