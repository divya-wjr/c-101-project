import dropbox
import os
from dropbox.files import WriteMode 
class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token

    def uploadFile(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.access_token)
        for root, dirs, files in os.walk(file_from):
             for i in files:
                local_path=os.path.join(root,i)

                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to, relative_path)
                with open(local_path,'rb') as f:
                    dbx.file_upload(f.read(),dropbox_path, mode=WriteMode('overwrite'))

def main():
    access_token = 'sl.Br4wzrsdC5qlah8wRAYyn1qD2luTfDSWRH4gQBLyDJ-5bn9R-uqQaSW-PL33N0WF7FDt6LHWw311IXvQF5hmsAMkYLO11G-SFPpqZDQMTw3RsrRK3HoE3BenVmvU4K-ovoIVqwNWbydj'
    transferData = TransferData(access_token)
    file_from = input("Enter the file path to UPLOAD")
    file_to =  input("Enter the file path to upload to dropbox")
    TransferData.upload_file(file_from,file_to)
    print("File has been moved....")
  
main()       
        