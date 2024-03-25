const { PDFDocument } = PDFLib;
    
async function showMeta() {
    const fileInput = document.getElementById('pdfpath');
    const file = fileInput.files[0];
  
    if (!file) {
      alert('Please select a file.');
      return;
    }
  
    try {
      const pdf1Bytes = await file.arrayBuffer();
      const pdfDoc = await PDFDocument.load(pdf1Bytes, { updateMetadata: false });
  
      // Log PDF metadata
      const title = pdfDoc.getTitle();
      const creator = pdfDoc.getCreator();
      const producer = pdfDoc.getProducer();
      const creationDate = pdfDoc.getCreationDate();
      const modDate = pdfDoc.getModificationDate();
      const keywords = pdfDoc.getKeywords();
      const author = pdfDoc.getAuthor();
      const subject = pdfDoc.getSubject();
  
      document.getElementById("title").value = title;
      document.getElementById("creator").value = creator;
      document.getElementById("producer").value = producer;
      document.getElementById("creationDate").value = creationDate;
      document.getElementById("modDate").value = modDate;
      document.getElementById("keywords").value = keywords;
      document.getElementById("author").value = author;
      document.getElementById("subject").value = subject;
      console.log('Title:', title);
      console.log('Author:', author);
      console.log('Subject:', subject);
      console.log('Creator:', creator);
      console.log('Keywords:', keywords);
      console.log('Producer:', producer);
      console.log('Creation Date:', creationDate);
      console.log('Modification Date:', modDate);
    } catch (error) {
      // Handle the error
      console.error('Error loading PDF document:', error);
      alert('Error loading PDF document: ' + error.message);
    }
  }
  
async function updatemeta(){
    const fileInput = document.getElementById('pdfpath');
    const file = fileInput.files[0];
    const fileName = file.name
    if (!file) {
      alert('Please select a file.');
      return;
    }
  
    const pdf1Bytes = await file.arrayBuffer();
    const pdfDoc = await PDFDocument.load(pdf1Bytes, { updateMetadata: false });
    const copyDoc = await pdfDoc.copy()

    const title = document.getElementById("title").value;
    const creator = document.getElementById("creator").value;
    const producer = document.getElementById("producer").value;
    const creationDate = document.getElementById("creationDate").value;
    const modDate = document.getElementById("modDate").value;
    let keywords = document.getElementById("keywords").value;
    const author = document.getElementById("author").value;
    const subject = document.getElementById("subject").value;
    keywords=keywords.split(',');
    copyDoc.setTitle(title)
    copyDoc.setAuthor(author)
    copyDoc.setSubject(subject)
    copyDoc.setKeywords(keywords)
    copyDoc.setProducer(producer)
    copyDoc.setCreator(creator)
    copyDoc.setCreationDate(new Date(creationDate))
    copyDoc.setModificationDate(new Date(modDate))


    const pdfBytes = await copyDoc.save()

    download(pdfBytes, fileName, "application/pdf");
}