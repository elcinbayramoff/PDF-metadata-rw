# Changing and Reading metadata of PDF


Once, when I edited and downloaded my CV from Canva, I encountered an unexpected issue: the title of the PDF file remained the same, making it seem unprofessional. Despite my attempts to edit it locally, I couldn't find a straightforward solution. Frustrated by this inconvenience, I sought a workaround and eventually turned to online platforms for editing metadata. However, this experience inspired me to take matters into my own hands and develop a solution tailored to my needs. Leveraging the power of ```tkinter``` and ```PyPDF2```, I embarked on creating a tool to efficiently manage PDF metadata. This project not only addressed my initial problem but also empowered me to proactively solve similar challenges in the future.

## Important!!!
Source code of PyPDF2 is overwritten and below code is added to the 156-165th lines of the ```_writer.py```
```
        info = DictionaryObject()
        info.update(
            {
                NameObject("/Producer"): create_string_object(
                    codecs.BOM_UTF16_BE + "".encode("utf-16be")
                )
            }
        )
        self._info = self._add_object(info)
```
Use command ```pip install -r requirements.txt``` to install all packages.
### Why overwritten?
While deleting all the metadata, it stills assign 'PyPDF2' value to the Producer key. That's why we need to change the source code.

