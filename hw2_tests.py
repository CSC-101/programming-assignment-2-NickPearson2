import data
import hw2
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    #Test point1 bottom left, point2 top right
    def test_create_rectangle1(self):
        point1 = data.Point(2,2)
        point2 = data.Point(10,10)
        top_left = data.Point(2,10)
        bottom_right = data.Point(10,2)
        result = data.Rectangle(top_left,bottom_right)
        self.assertEqual(hw2.create_rectangle(point1,point2), result)
    def test_create_rectangle2(self):
        point1 = data.Point(10,10)
        point2 = data.Point(2,2)
        top_left = data.Point(2,10)
        bottom_right = data.Point(10,2)
        result = data.Rectangle(top_left,bottom_right)
        self.assertEqual(hw2.create_rectangle(point1,point2), result)
    #Test point1 bottom right, point2 top left
    def test_create_rectangle3(self):
        point1 = data.Point(5,3)
        point2 = data.Point(2,10)
        top_left = data.Point(2,10)
        bottom_right = data.Point(5,3)
        result = data.Rectangle(top_left,bottom_right)
        self.assertEqual(hw2.create_rectangle(point1,point2), result)
    #Test point2 bottom right, point1 top left
    def test_create_rectangle4(self):
        point1 = data.Point(2,10)
        point2 = data.Point(5,3)
        top_left = data.Point(2,10)
        bottom_right = data.Point(5,3)
        result = data.Rectangle(top_left,bottom_right)
        self.assertEqual(hw2.create_rectangle(point1,point2), result)
    # Part 2
    def test_shorter_duration_than1(self):
        duration1 = data.Duration(5,5)
        duration2 = data.Duration(10,10)
        print("Test1")
        self.assertEqual(hw2.shorter_duration_than(duration1,duration2), True)
        print("test2")
        self.assertEqual(hw2.shorter_duration_than(duration2,duration1), False)
    def test_shorter_duration_than2(self):
        duration1 = data.Duration(5,5)
        duration2 = data.Duration(5,10)
        self.assertEqual(hw2.shorter_duration_than(duration1,duration2), True)
        self.assertEqual(hw2.shorter_duration_than(duration2,duration1), False)
    # Part 3
    def test_song_shorter_than(self):
        duration1 = data.Duration(5,5)
        duration2 = data.Duration(5,10)
        duration3 = data.Duration(10,10)
        song1 = data.Song("Tom Petty","Breakdown",duration1)
        song2 = data.Song("Pink Floyd","Pigs",duration3)
        song_list = [song1,song2]
        self.assertEqual(hw2.song_shorter_than(song_list,duration2), [song1])
    def test_song_shorter_than2(self):
        duration1 = data.Duration(5,5)
        duration2 = data.Duration(5,10)
        duration3 = data.Duration(10,10)
        song1 = data.Song("Tom Petty","Breakdown",duration1)
        song2 = data.Song("Pink Floyd","Pigs",duration2)
        song_list = [song1,song2]
        self.assertEqual(hw2.song_shorter_than(song_list,duration3), [song1,song2])
    # Part 4
    def test_running_time(self):
        duration1 = data.Duration(5, 5)
        duration2 = data.Duration(5, 10)
        duration3 = data.Duration(10, 10)
        song1 = data.Song("Tom Petty", "Breakdown", duration1)
        song2 = data.Song("Pink Floyd", "Pigs", duration3)
        song3 = data.Song("Dire Straits", "Down to the Waterline",duration2)
        song_list = [song1,song2,song3]
        result = data.Duration(25,30)
        self.assertEqual(hw2.running_time(song_list,[0,2,1,0]), result)
    def test_running_time2(self):
        duration1 = data.Duration(5, 30)
        duration2 = data.Duration(5, 10)
        duration3 = data.Duration(10, 10)
        song1 = data.Song("Tom Petty", "Breakdown", duration1)
        song2 = data.Song("Pink Floyd", "Pigs", duration3)
        song3 = data.Song("Dire Straits", "Down to the Waterline",duration2)
        song_list = [song1,song2,song3]
        result = data.Duration(26,20)
        self.assertEqual(hw2.running_time(song_list,[0,2,1,0]), result)
    # Part 5
    def test_validate_route(self):
        city_links = [['san luis obispo', 'santa margarita'],
            ['san luis obispo', 'pismo beach'],
            ['atascadero', 'santa margarita'],
            ['atascadero', 'creston']]
        route = ['san luis obispo', 'santa margarita', 'atascadero']
        self.assertEqual(hw2.validate_route(city_links, route), True)
    def test_validate_route2(self):
        city_links = [['san luis obispo', 'santa margarita'],
            ['san luis obispo', 'pismo beach'],
            ['atascadero', 'santa margarita'],
            ['atascadero', 'creston']]
        route = ['san luis obispo', 'atascadero']
        route2 = []
        self.assertEqual(hw2.validate_route(city_links, route), False)
        self.assertEqual(hw2.validate_route(city_links, route2), True)

    # Part 6
    def test_longest_repetition(self):
        list =[1, 1, 2, 2, 1, 1, 1, 3]
        self.assertEqual(hw2.longest_repetition(list), 4)
    def test_longest_repetition2(self):
        list =[1, 1, 2, 2, 2, 2, 1, 1, 1, 3]
        self.assertEqual(hw2.longest_repetition(list), 2)
    def test_longest_repetition3(self):
        list =[1, 1, 2, 2, 1, 1, 3]
        self.assertEqual(hw2.longest_repetition(list), 0)




if __name__ == '__main__':
    unittest.main()
