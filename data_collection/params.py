
BASE_URL="https://api.archives-ouvertes.fr/search/?"
DATA_DIR="/Users/dungaoda/Documents/projetfindetude/data_collection/data"

HTTP_OK=200

HTTP_NOT_FOUND=404
HTTP_BAD_REQUEST=400
HTTP_FORBIDDEN=403

HTTP_INTERNAL_SERVER_ERROR=500
HTTP_SERVICE_UNAVAILABE=503

NOT_FOUND_MSG="The ressource you are looking for is not found. Probably it has been moved from this location. Check your API URI."
BAD_REQUEST_MSG="The request can't be understood by the server. Probably you are missing a parameter or you are passing the wrong parameters."
FORBIDDEN_MSG = "You have not the right to access this ressouce. Please contact the ressouce administrator."
INTERNAL_SERVER_ERROR_MSG="The server encounters an internal issue. You could try again later or contact the server administrator"
SERVICE_UNAVAILABLE_MSG="The service you are looking for it is not available at the moment."

CSV_FILE_HEADER="Title,Abstract,Keywords,AuthorNames"

FILE_NOT_EXIST_MSG="The file you are looking for does not exists in the current directory. We will create a new one."
DIR_NOT_EXISTS_MSG="The directory the you are looking for does not exists"