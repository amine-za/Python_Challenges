"""
    Your task is to determine what Bob will reply to someone when they say something to him or ask him      a question. Bob only ever answers one of five things:
"""

def response(hey_bob):
    trimmed_hey = hey_bob.rstrip()
    
    if not hey_bob.strip():
        return "Fine. Be that way!" 
    if hey_bob.isupper() and trimmed_hey[len(trimmed_hey) - 1] == '?':
        return "Calm down, I know what I'm doing!"
    if trimmed_hey[len(trimmed_hey) - 1] == '?':
        return "Sure."
    if hey_bob.isupper():
        return "Whoa, chill out!"
    else:
        return "Whatever." 
