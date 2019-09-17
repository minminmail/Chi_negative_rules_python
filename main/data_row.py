# store the each row, class result , feature values, label values
# added by rui for negative rule
class data_row:
    class_value = None
    feature_values = []
    label_values = []

    def __init__(self, class_value, feature_array, label_array):
        print("__init__ of data_row")
        self.class_value = class_value
        self.feature_values = feature_array
        self.label_values = label_array