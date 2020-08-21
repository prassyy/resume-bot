# Resume Bot
As much as I hate to think of my resume getting lost amongst thousands of others while getting filtered by an ATS, I appreciate it's necessity. After doing this for a dozen times, I started seeing a pattern and wanted to automate this stuff too!

Matching the Resumes for the skills that you are looking for is essentially what you want to do. I came up with this python script which looks through the text in PDFs and summarises each of their skills. This isn't a representation of more complex systems designed to dedicatedly this stuff, but enough to save a bunch of time.

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


