from os.path import exists
import logging
logging.basicConfig(level=logging.DEBUG,filename="log_find_replace.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

def find_and_replace(filename):
  try:
    fexists = exists(filename)
    if fexists:
      with open(filename, 'r') as file:
        filedata = file.read()
      find_word = input("Enter the word to find for replacing :- ")
      if find_word in filedata:
        replace_word = input("Enter the word to replace :- ")
        filedata = filedata.replace(find_word,replace_word)
        logging.info(filedata)
        with open(filename,'w') as file:
            file.write(filedata)
      else:
        logging.error("The entered word not found in the file")
    else:
      logging.info("The file given doesn't exists")
  except Exception as e:
    logging.exception("Exeception occured during the execution" + str(e))


if __name__ == "__main__":
  file_path = input("Enter the file path :- ")
  find_and_replace(file_path)
  