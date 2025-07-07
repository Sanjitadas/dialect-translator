import requests

def correct_grammar(text, lang="en-US"):
    try:
        url = "https://api.languagetool.org/v2/check"
        data = {
            "text": text,
            "language": lang
        }
        response = requests.post(url, data=data)
        result = response.json()

        corrected = text
        for match in reversed(result["matches"]):
            start = match["offset"]
            end = start + match["length"]
            replacements = match.get("replacements", [])
            if replacements:
                replacement = replacements[0]["value"]
                corrected = corrected[:start] + replacement + corrected[end:]
        return corrected
    except Exception as e:
        return f"Grammar Correction Error: {str(e)}"

