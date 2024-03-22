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
    writer.add_metadata(
    {'/Creator': Creator,
    '/Producer': Producer,
    '/CreationDate': back_formatter(CreationDate),
    '/ModDate': back_formatter(ModDate),
    '/Keywords': KeyWords,
    '/Author': Author,
    '/Title': Title}
    )

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
        Creator, Producer, CreationDate, ModDate, Keywords, Author, Title = \
            meta['/Creator'], meta['/Producer'], meta['/CreationDate'], meta['/ModDate'], meta['/Keywords'], meta['/Author'], meta['/Title']

        Cdate = formatter(CreationDate)
        CreationDate = toLocalUTC(int(Cdate['year']), int(Cdate['month']), int(Cdate['day']), \
            int(Cdate['hour']), int(Cdate['minute']), int(Cdate['second']))
        Cdate = formatter(ModDate)
        ModDate = toLocalUTC(int(Cdate['year']), int(Cdate['month']), int(Cdate['day']), \
            int(Cdate['hour']), int(Cdate['minute']), int(Cdate['second']))
        return [Creator, Producer, CreationDate, ModDate, Keywords, Author, Title]
    else:
        return False
