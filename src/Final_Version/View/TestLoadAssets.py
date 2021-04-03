import unittest
import LoadAssets
import time
class LoadAssetsTest(unittest.TestCase):
    def setUp(self):
       self.__target_time = 5
       self.__time_taken = 0

    def test_load_floor(self):
        now = time.time()
        image = LoadAssets.load_floor()
        self.__time_taken += time.time() - now
        self.assertLessEqual(self.__time_taken, self.__target_time)
    
    def test_load_background(self):
        now = time.time()
        image = LoadAssets.load_background()
        self.__time_taken += time.time() - now
        self.assertLessEqual(self.__time_taken, self.__target_time)

    def test_load_character(self):
            now = time.time()
            image = LoadAssets.load_character()
            self.__time_taken += time.time() - now
            self.assertLessEqual(self.__time_taken, self.__target_time)

    def test_load_obstacles(self):
            now = time.time()
            image = LoadAssets.load_all_obstacles()
            self.__time_taken += time.time() - now
    def test_load_powerups(self):
            now = time.time()
            image = LoadAssets.load_all_powerups()
            self.__time_taken += time.time() - now
            self.assertLessEqual(self.__time_taken, self.__target_time)

    def test_load_main_menu(self):
            now = time.time()
            image = LoadAssets.load_main_menu()
            self.__time_taken += time.time() - now
            self.assertLessEqual(self.__time_taken, self.__target_time)
    def test_load_pause_menu(self):
            now = time.time()
            image = LoadAssets.load_pause_menu()
            self.__time_taken += time.time() - now
            self.assertLessEqual(self.__time_taken, self.__target_time)
    def test_load_end_menu(self):
            now = time.time()
            image = LoadAssets.load_end_menu()
            self.__time_taken += time.time() - now
            self.assertLessEqual(self.__time_taken, self.__target_time)
    def test_load_setting_menu(self):
            now = time.time()
            image = LoadAssets.load_settting_menu()
            self.__time_taken += time.time() - now
            self.assertLessEqual(self.__time_taken, self.__target_time)
    def test_load_instruction_menu(self):
            now = time.time()
            image = LoadAssets.load_instruction_menu()
            self.__time_taken += time.time() - now
            self.assertLessEqual(self.__time_taken, self.__target_time)
    def test_load_sound(self):
            now = time.time()
            image = LoadAssets.load_sound()
            self.__time_taken += time.time() - now
            self.assertLessEqual(self.__time_taken, self.__target_time)

if  __name__  == '__main__ ':
    # loadTestsFromTestCase  looks  for  methods  that
    # start  with  the  word "test"
    suite = unittest.TestLoader().loadTestsFromTestCase(Box3DTest)
    suite.run()

