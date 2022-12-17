import  metaData
import metaData.extractTitleAndSourceFromArabicDataset as ex
import  metaData.metaData as md
import metaData.keyWords as kw
import metaData.keyWordsUsingYake as kwy
filePath = "E:\\computers\\level 4\\semester 1\\selected 3\\project\\arabiya\\Test\\Medical\\107-مليون-إصابة-بأمراض-الكلى-سنوياً-بسبب-تلوث-الهواء-.txt"
path = "E:\\computers\\level 4\\semester 1\\selected 3\\project\\arabiya\\Test\\Medical"
filename = "107-مليون-إصابة-بأمراض-الكلى-سنوياً-بسبب-تلوث-الهواء-.txt"
body = ex.extractTitleAndPublisher(filePath)
md.get_file_metadata(path, filename)
keywords = kw.get_keywordsFromText(body)
kw.print_results(keywords)
keywords = kwy.yakeKeyWords(body)
print(keywords)

