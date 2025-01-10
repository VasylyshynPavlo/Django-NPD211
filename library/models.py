from mongoengine import (
    Document,
    StringField,
    EmbeddedDocumentListField,
    EmbeddedDocument
)


class Example(EmbeddedDocument):
    text = StringField(required=True)
    translate = StringField()

    def __str__(self):
        return self.text


class Word(EmbeddedDocument):
    text = StringField(required=True)
    description = StringField()
    translate = StringField()
    examples = EmbeddedDocumentListField(Example)

    def __str__(self):
        return self.text


class WordsCollection(Document):
    title = StringField()
    userId = StringField(required=True)
    language = StringField(required=True)
    words = EmbeddedDocumentListField(Word)

    def __str__(self):
        return self.title + self.language
