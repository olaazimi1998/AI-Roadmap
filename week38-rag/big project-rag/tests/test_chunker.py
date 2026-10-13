from app.chunker import split_into_chunks


def test_chunks_cover_text():
    text = "A" * 2500

    chunks = split_into_chunks(
        text,
        chunk_size=1000,
        overlap=150
    )

    assert len(chunks) == 3
    assert all(len(chunk) <= 1000 for chunk in chunks)


def test_empty_text():
    chunks = split_into_chunks("")

    assert chunks == []


def test_invalid_chunk_size():
    try:
        split_into_chunks("Hello", chunk_size=0)
    except ValueError:
        pass
    else:
        raise AssertionError("Expected ValueError")


if __name__ == "__main__":
    test_chunks_cover_text()
    test_empty_text()
    test_invalid_chunk_size()

    print("All chunker tests passed!")