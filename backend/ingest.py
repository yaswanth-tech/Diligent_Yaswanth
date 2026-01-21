from vector_store import index_texts

# Tiny helper script to push sample docs once.
sample_docs = [
    "We ship fast answers for customer questions.",
    "Support hours: 9am-6pm PST Monday through Friday.",
    "Pricing plans include Starter, Growth, and Scale.",
]

index_texts([(f"seed-{i}", text) for i, text in enumerate(sample_docs)])
print("Sample documents indexed.")
