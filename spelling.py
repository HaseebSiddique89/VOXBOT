from gingerit.gingerit import GingerIt

# Create an instance of GingerIt
parser = GingerIt()

# Perform spell correction
def correct_spelling(text):
    result = parser.parse(text)
    corrected_text = result['result']
    return corrected_text


