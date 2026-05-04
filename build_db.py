import chromadb

SEPARATOR = '-' * 70

client = chromadb.PersistentClient("./chroma_db")


def load_chunks(filename):
    with open(filename) as f:
        text = f.read()

    sections = text.split(SEPARATOR)

    chunks = []
    for section in sections:
        chunks.append(section.strip())
    return chunks
    


chunks = load_chunks('roster_2026.txt')


files_and_collections = [
    ('roster_2026.txt', roster),
    ('scouting_2027.txt', scouting),
    ('opponents_2026.txt', opponents)
]

