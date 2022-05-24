chunk_size = 1
with open("test.jpg", 'rb') as donor:
    with open("test.jpg", 'wb') as receiver:
        while True:
            chunk = donor.read(chunk_size)
            if not chunk:
                break
            receiver.write(chunk)

print("done!")


