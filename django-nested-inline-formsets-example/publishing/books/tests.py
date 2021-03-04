import pytest
import ipdb

from publishing.books.forms import PublisherBooksWithImagesFormset
from publishing.books.models import Publisher


@pytest.mark.django_db
def test_is_valid():
    MyFormSet = PublisherBooksWithImagesFormset(extra=1)
    obj = Publisher.objects.create(name="Valentyn")
    data = {
        "books-TOTAL_FORMS": "1",
        "books-INITIAL_FORMS": "0",
        "books-MIN_NUM_FORMS": "0",
        "books-MAX_NUM_FORMS": "1000",
        "books-0-title": "harry potter",
        "books-0-id": "",
        "books-0-publisher": obj.id,
        "bookimage-books-0-images-TOTAL_FORMS": "1",
        "bookimage-books-0-images-INITIAL_FORMS": "0",
        "bookimage-books-0-images-MIN_NUM_FORMS": "0",
        "bookimage-books-0-images-MAX_NUM_FORMS": "1000",
        "bookimage-books-0-images-0-alt_text": "picture",
        "bookimage-books-0-images-0-id": "",
        "bookimage-books-0-images-0-book": "",
    }
    formset = MyFormSet(data, instance=obj)
    ipdb.set_trace()
    assert formset.is_valid()
