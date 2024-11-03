from abc import ABC, abstractmethod # import abstract class python infrastracture
import os 
import data_collection.params as p 

class FileWritingStrategy(ABC):
    @abstractmethod
    def write_to_file(self, file_path: str, data: str):
        pass



################################
##### CLASS IMPLEMENTATION #####
################################

class CSV_Writer(FileWritingStrategy) : 

  def __init__(self) -> None:
    self.check = True 

  def write_header(self, file_path, header_str) : 
    with open(file_path, 'w', encoding='utf-8') as txt_file:
      txt_file.write(header_str + "\n")

  def write_to_file(self, file_path : str, data : str):
    with open(file_path, 'a', encoding='utf-8') as txt_file:
      txt_file.write(f"{data}")
  




