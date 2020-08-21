# Resume Bot
As much as I hate to think my resume getting lost amongst thousands of other resumes while getting filtered by an ATS, I appreciate the necessity for it. After doing this for a dozen files, I started seeing a pattern and wished I could somehow automate this stuff!

Matching the Resumes for the roles using the skills that you are looking for is essentially what you want to do. I came up with this python script which looks through the text in PDFs and summarises each of their skills. This isn't a representation of more complex systems designed to dedicatedly this stuff, but sophisticated enough to save a bunch of time.

## Install
I used this PDF reader called [Slate]([https://github.com/timClicks/slate](https://github.com/timClicks/slate)). It depends on PDFMiner. To install it,
```
pip3 install slate3k
```

## Run
- *keywords.txt* - This is where you list the things that you want to look for in the Stack of Resumes
- */feed*- Load this directory with all the files you have
- Run `python3 resume-bot.py`
- Your summary will be in `summary.txt`.

