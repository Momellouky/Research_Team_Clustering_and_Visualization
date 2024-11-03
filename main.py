import data_collection.collect as collect 
import data_collection.params as p
import data_collection.writer as writer
import sys 

collector = collect.Data_Collector()
csv_writer = writer.CSV_Writer()

def list2string(list) :  #unused

    if len(list) == 0 : 
        return 'N/A' 
    # Join the elements of the list with a comma as a separator
    result_string = ",".join(list)
    result_string.replace('"', '\"' )
    
    return "\"" + result_string + "\"" 

def main():

    # print("first arg : ", sys.argv[1])

    teams = ['LAB-STICC_INUIT', 'LAB-STICC_RAMBO', 'LAB-STICC_COMMEDIA']

    for team in teams:

        publications = collector.get_team_publications(team)
        csv_writer.write_to_file(file_path=f"{p.DATA_DIR}/{team}_data.csv", data=publications)

if __name__ == "__main__":
    main()
