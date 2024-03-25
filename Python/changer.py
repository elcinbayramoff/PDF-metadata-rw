from PyPDF2 import PdfReader,PdfWriter
from date import toLocalUTC,formatter,back_formatter
def MetaReader(path_to_pdf):
    reader = PdfReader(path_to_pdf)
    meta = reader.metadata
    return meta

def MetaWriter(Creator,Producer,CreationDate,ModDate,KeyWords,Author,Title,path_to_pdf):
    writer = PdfWriter()
    reader = PdfReader(path_to_pdf)
    
    for page in reader.pages:
        writer.add_page(page)
    metadata = {
        '/Creator': Creator,
        '/Producer': Producer,
        '/Keywords': KeyWords,
        '/Author': Author,
        '/Title': Title
    }
    
    if CreationDate:
        metadata['/CreationDate'] = back_formatter(CreationDate)
    else:
        metadata['/CreationDate'] = CreationDate
    if ModDate:
        metadata['/ModDate'] = back_formatter(ModDate)
    else:
        metadata['/ModDate'] = ModDate
    writer.add_metadata(metadata)
    with open(path_to_pdf, "wb") as f:
        writer.write(f)
def PdfMeta(path_to_pdf):
    with open(path_to_pdf, 'rb') as f:
        file_signature = f.read(4)
        if file_signature== b'%PDF':
            state=True
        else: state= False
    if state:
        meta = MetaReader(path_to_pdf)
        # try:
        Creator, Producer, CreationDate, ModDate, Keywords, Author, Title = \
            meta['/Creator'], meta['/Producer'], meta['/CreationDate'], meta['/ModDate'], meta['/Keywords'], meta['/Author'], meta['/Title']
        Cdate = formatter(CreationDate)
        if CreationDate:
            CreationDate = toLocalUTC(int(Cdate['year']), int(Cdate['month']), int(Cdate['day']), \
                int(Cdate['hour']), int(Cdate['minute']), int(Cdate['second']))
            Cdate = formatter(ModDate)
        if ModDate:
            ModDate = toLocalUTC(int(Cdate['year']), int(Cdate['month']), int(Cdate['day']), \
                int(Cdate['hour']), int(Cdate['minute']), int(Cdate['second']))
    
        # except:
        #     Creator, Producer, CreationDate, ModDate, Keywords, Author, Title='','','','','','',''
        return [Creator, Producer, CreationDate, ModDate, Keywords, Author, Title]
    else:
        return False
