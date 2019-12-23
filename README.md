# pdf-academic-analyzer

## Todo

[ ] Sentiment Analysis - show most negative and most positive sentences

[ ] RESEARCH possibility of adding custom nounphrases for textblob's `noun_phrases` feature

[ ] Output title (test various ways to identify)

[ ] INIT web UI

## Up and running

1. `docker-compose up`
2. `docker-compose exec app bash`
Inside the container:
3. `pip install -r requirements.txt`
4. `python main.py FILENAME_IN_INPUT_FOLDER`


## Notes

Target file must be put inside `app/input`

```python
import pdftotext

# Load your PDF
with open("lorem_ipsum.pdf", "rb") as f:
    pdf = pdftotext.PDF(f)

# If it's password-protected
with open("secure.pdf", "rb") as f:
    pdf = pdftotext.PDF(f, "secret")

# How many pages?
print(len(pdf))

# Iterate over all the pages
for page in pdf:
    print(page)

# Read some individual pages
print(pdf[0])
print(pdf[1])

# Read all the text into one string
print("\n\n".join(pdf))
```