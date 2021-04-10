import ipdb
import pytest
from django.core.files.uploadedfile import SimpleUploadedFile
from PIL import Image

from config import settings
from publishing.books.forms import PublisherBooksWithImagesFormset
from publishing.books.models import Publisher


@pytest.mark.django_db
def test_is_valid(tmpdir):
    temp_img = tmpdir.join("temp.png")
    img = Image.new("RGB", (200, 30), "#ddd")
    img.save(str(temp_img))

    settings.MEDIA_ROOT = tmpdir
    upload_file = SimpleUploadedFile(
        name="temp.png",
        content=open(str(temp_img), "rb").read(),
        content_type="image/png",
    )
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
    formset = MyFormSet(
        data,
        files={
            "bookimage-books-0-images-0-image": upload_file,
        },
        instance=obj,
    )
    assert formset.is_valid()
