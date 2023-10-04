import sys
import unittest
import subprocess
from lab1.task1.task1 import task1_solv
sys.path.append("D:/BSUIR/5sem/VPO/")


class Task1Test(unittest.TestCase):

    def test_hello_world(self):
        task1_solv()
        proc = subprocess.Popen(['python', 'task1/tests/test_task1.py'], stdout=subprocess.PIPE)
        byte_hello = str(proc.stdout.readline().strip())
        byte_andhiagain = str(proc.stdout.readline().strip())
        byte_exclamations = str(proc.stdout.readline().strip())
        str_hello = byte_hello[2:len(byte_hello.strip()) - 1]
        str_andhiagain = byte_andhiagain[2:len(byte_andhiagain.strip()) - 1]
        str_exclamations = byte_exclamations[2:len(byte_exclamations.strip()) - 1]
        result = str_hello, str_andhiagain, (5 <= str_exclamations.count("!") <= 50)
        self.assertEqual(result, ("Hello, world!", "Andhiagain!", True))


if __name__ == '__main__':
    unittest.main()
