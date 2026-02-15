"""
Simple Sentiment Analysis Chatbot
A beginner-friendly GenAI project using transformers

Requirements:
pip install transformers torch
"""

from transformers import pipeline

class SentimentAnalyzer:
    def __init__(self):
        # Load pre-trained sentiment analysis model
        print("Loading sentiment analysis model...")
        self.analyzer = pipeline("sentiment-analysis", 
                                model="distilbert-base-uncased-finetuned-sst-2-english")
        print("Model loaded successfully!\n")
    
    def analyze_text(self, text):
        """Analyze sentiment of given text"""
        result = self.analyzer(text)[0]
        label = result['label']
        score = result['score']
        
        # Format output
        sentiment = "Positive 😊" if label == "POSITIVE" else "Negative 😔"
        confidence = f"{score * 100:.2f}%"
        
        return sentiment, confidence
    
    def run_chatbot(self):
        """Interactive chatbot loop"""
        print("=" * 50)
        print("  Sentiment Analysis Chatbot")
        print("=" * 50)
        print("Type any text to analyze its sentiment")
        print("Type 'quit' to exit\n")
        
        while True:
            user_input = input("You: ").strip()
            
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("\nGoodbye! 👋")
                break
            
            if not user_input:
                print("Please enter some text.\n")
                continue
            
            sentiment, confidence = self.analyze_text(user_input)
            print(f"Sentiment: {sentiment}")
            print(f"Confidence: {confidence}\n")


def main():
    # Initialize and run the chatbot
    bot = SentimentAnalyzer()
    bot.run_chatbot()


if __name__ == "__main__":
    main()
