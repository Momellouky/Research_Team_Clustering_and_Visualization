import requests
import csv
import data_collection.params as p
import data_collection.writer as writer 

class Data_Collector : 
  '''
  Data_Collector : a singleton class that allow to request the following
  ressources from the HAL API:
    Title, Abtract and Keywords of all publications of the following teams:
      LAB-STICC_INUIT, LAB-STICC_RAMBO and LAB-STICC_COMMEDIA 
  It queries these ressources and write them in a txt file inder the {data} folder.
  '''
    
  _instance = None # implement the singleton design patter

  def __new__(cls):
    if not cls._instance:
        cls._instance = super(Data_Collector, cls).__new__(cls)
        # Initialize the instance (e.g., set up API connection)
    return cls._instance
  
  def __init__(self) -> None:
      self.base_url = p.BASE_URL
    


  def get_team_publications(self, team_name):
      '''
      Query the HAL API to get the publications of a team inside the interaction pole. 
      @params team_name : the name of team which we want its publications
      @returns a list of the publications found in the HAL repo.
      '''
      params = {
          'fl': 'title_s,abstract_s,keyword_s,authFullName_s,publicationDateY_i,language_s',
          'fq': f'collCode_s:{team_name} AND publicationDateY_i:[2020 TO 2023]',
          'wt': 'csv',
          'lang' : 'en',
          'rows': 100  # The number of rows per request
      }

      response = requests.get(p.BASE_URL, params=params)
      res = self._get_response(response=response) 
      return res

  ######################################################
  ################ PRIVATE METHODS ####################
  ######################################################
      
  def _get_response(self, response) : 
    STATUS_CODE= response.status_code
    if STATUS_CODE == p.HTTP_OK : 
       return response.text
    elif STATUS_CODE == p.HTTP_NOT_FOUND : 
      print(p.NOT_FOUND_MSG)
      return []
    elif STATUS_CODE == p.HTTP_BAD_REQUEST : 
      print(p.BAD_REQUEST_MSG)
      return []
    elif STATUS_CODE == p.HTTP_FORBIDDEN:
        print(p.FORBIDDEN_MSG)
        return []
    elif STATUS_CODE == p.HTTP_INTERNAL_SERVER_ERROR:
        print(p.INTERNAL_SERVER_ERROR_MSG)
        return []
    elif STATUS_CODE == p.HTTP_SERVICE_UNAVAILABE : 
        print(p.SERVICE_UNAVAILABLE_MSG)
        return []
    else : 
      print(f"Error: {response.status_code}")
      return []

