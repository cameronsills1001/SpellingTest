__author__ = 'cameron'

class Read_Write:

    def write_list(self, words):
        #used to make a new list of words in a file
        self.words = words
        word_list = open("word_list.txt", "w")
        for i in words:
            word_list.write("%s\n" % i)
        word_list.close()


    def read_list(self):
        #used to retrieve a previously made list of words
        data = open("word_list.txt", "r")
        word_list = [str(e.strip()) for e in data]
        data.close()
        return word_list

    def set_points(self, points):
        #method for setting points
        self.points = points
        points = str(points)
        point_count = open("points.txt", "w")
        point_count.write(points)
        point_count.close()

    def get_points(self):
        #method for getting points
        data = open('points.txt', "r")
        points = data.read()
        return int(points)



