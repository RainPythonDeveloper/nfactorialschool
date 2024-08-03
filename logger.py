class Logger:
    def __init__(self):
        self.message_dict = {}
        self.capacity = 100

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.message_dict or timestamp >= self.message_dict[message]:
            self.message_dict[message] = timestamp + 10
            if len(self.message_dict) > self.capacity:
                self._clean_old_messages(timestamp)
            return True
        return False

    def clean(self, timestamp: int) -> bool:
        if any(ts == timestamp for ts in self.message_dict.values()):
            return False
        self._clean_old_messages(timestamp)
        return True

    def loggerSize(self) -> int:
        return len(self.message_dict)

    def _clean_old_messages(self, current_timestamp: int):
        to_remove = [msg for msg, ts in self.message_dict.items() if ts <= current_timestamp]
        for msg in to_remove:
            del self.message_dict[msg]

if __name__ == "__main__":
    logger = Logger()

    print(logger.shouldPrintMessage(1, "foo"))  
    print(logger.shouldPrintMessage(2, "bar")) 
    print(logger.shouldPrintMessage(3, "foo"))  
    print(logger.shouldPrintMessage(8, "bar"))  
    print(logger.shouldPrintMessage(10, "foo")) 
    print(logger.shouldPrintMessage(11, "foo")) 

    print(logger.loggerSize()) 
    print(logger.clean(11))  
    print(logger.clean(12)) 
