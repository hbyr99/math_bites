# Import dependencies
import unittest
import os.path
from os import path
from DB_Func import DB_Func


class Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self
    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio    # free up some memory
        sys.stdout = self._stdout

class TestDB_Func(unittest.TestCase):
    def test_createDB(self):
        try:
            testDB = DB_Func()
            testDB.createDB('test')
        except Exception as e:
            raise AssertionError('Test failed!')

    def test_addEntry(self):
        testDB = DB_Func()
        testDB.createDB('test')
        testDB.addEntry('test1', 2)
        dbcur = testDB.connection
        result = dbcur.execute("""
            SELECT COUNT(*)
            FROM information_schema.tables
            WHERE table_name = 'test1'
            """)
        
        assert(result != None)

    def test_showScatter(self):
        testDB = DB_Func()
        testDB.createDB('test')
        testDB.addEntry('test1', 2)
        testDB.showScatter('test1')
        assert(path.exists('test1.html'))

    def test_deleteDB(self):
        try:
            testDB = DB_Func()
            testDB.createDB('test')
            testDB.addEntry('test1', 2)
            testDB.deleteDB('test')
        except Exception as e:
            raise AssertionError('Test failed!')
        
    
if __name__ == '__main__':
    unittest.main()