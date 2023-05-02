class Dashboard:

    def __init__(self):
        pass

    def display_processed_data(self, data):
        print("Median: {median}, Sum: {sum}, Mean: {mean}\n".format(median=data[0], sum=data[1], mean=data[2]))


    def display_raw_data(self, data):
        for s in data:
            print(s)
