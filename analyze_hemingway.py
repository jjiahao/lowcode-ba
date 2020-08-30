import boto3


text = """
Then there was another thing. He had been reading W. H. Hudson. That sounds like an innocent occupation, but Cohn had read and reread "The Purple Land." "The Purple Land" is a very sinister book if read too late in life. It recounts splendid imaginary amorous adventures of a perfect English gentleman in an intensely romantic land, the scenery of which is very well described. For a man to take it at thirty-four as a guide-book to what life holds is about as safe as it would be for a man of the same age to enter Wall Street direct from a French convent, equipped with a complete set of the more practical Alger books. Cohn, I believe, took every word of "The Purple Land" as literally as though it had been an R. G. Dun report. You understand me, he made some reservations, but on the whole the book to him was sound. It was all that was needed to set him off. I did not realize the extent to which it had set him off until one day he came into my office.
"""

client = boto3.client('comprehend')
response = client.batch_detect_key_phrases(
    TextList=[
        text,
    ],
    LanguageCode='en')
print(response)