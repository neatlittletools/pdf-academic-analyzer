# pdf-academic-analyzer

## Todo

[ ] RESEARCH possibility of adding custom nounphrases for textblob's `noun_phrases` feature

[ ] Output title (test various ways to identify)

[ ] INIT web UI

[ ] change from Pickle to JSON

[ ] parse all Classes and namedtuples in dicts into JSONs

## Up and running

1. `docker-compose up`
2. In a new terminal shell: `docker-compose exec app bash`
Inside the container:
3. `./setup.sh` to run pip install using requirements.txt
4. `python main.py FILENAME_IN_INPUT_FOLDER`


## Notes

- Target file must be put inside `app/input`
- currently only takes in PDF files

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