import random

class AIQuoteGenerator:
    def __init__(self):
        self.start_phrases = [
            "Artificial Intelligence is",
            "Machine learning will",
            "Neural networks are",
            "In the future, AI will",
            "Deep learning empowers",
            "AI-driven systems can",
            "The power of AI lies in"
        ]
        
        self.middle_phrases = [
            "revolutionizing the way we",
            "paving the path to",
            "creating unprecedented possibilities for",
            "transforming industries with",
            "unlocking the potential of",
            "bridging the gap between humans and",
            "accelerating innovations in"
        ]
        
        self.end_phrases = [
            "efficiency and automation.",
            "a smarter tomorrow.",
            "predictive analytics.",
            "self-learning systems.",
            "autonomous technologies.",
            "the next big disruption.",
            "complex problem-solving."
        ]

    def generate_quote(self):
        start = random.choice(self.start_phrases)
        middle = random.choice(self.middle_phrases)
        end = random.choice(self.end_phrases)
        return f"{start} {middle} {end}"

def main():
    generator = AIQuoteGenerator()
    for _ in range(5):  # Generate 5 random quotes
        print(generator.generate_quote())

if __name__ == "__main__":
    main()
