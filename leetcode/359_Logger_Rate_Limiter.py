from collections import deque


class Logger:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.cur_msg = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        if message not in self.cur_msg:
            self.cur_msg[message] = timestamp
            return True

        if timestamp - self.cur_msg[message] >= 10:
            self.cur_msg[message] = timestamp
            return True

        return False


class LoggerQueue:
    def __init__(self):
        self._msg_queue = deque()
        self._msg_set = set()

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        while self._msg_queue:
            msg, ts = self._msg_queue[0]
            if timestamp - ts >= 10:
                self._msg_queue.popleft()
                self._msg_set.remove(msg)
            else:
                break

        if message not in self._msg_set:
            self._msg_set.add(message)
            self._msg_queue.append((message, timestamp))
            return True
        return False


def check_case(logger: Logger):
    assert logger.shouldPrintMessage(1, "foo") == True
    assert logger.shouldPrintMessage(2, "bar") == True
    assert logger.shouldPrintMessage(3, "foo") == False
    assert logger.shouldPrintMessage(8, "bar") == False
    assert logger.shouldPrintMessage(10, "foo") == False
    assert logger.shouldPrintMessage(11, "foo") == True
    assert logger.shouldPrintMessage(13, "bar") == True


def test_solution():
    check_case(Logger())


def test_solution_queue():
    check_case(LoggerQueue())
