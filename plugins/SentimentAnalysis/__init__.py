from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
from nextcord.ext import commands

from Plugin import AutomataPlugin

nltk.downloader.download('vader_lexicon')


class SentimentAnalysis(AutomataPlugin):
    """NLTK Sentiment Analyzer"""

    sia = SentimentIntensityAnalyzer()

    @commands.command()
    async def sentiment(self, ctx, *, argument):
        """Replies with the sentiment of the sentence"""

        output_template = "<@{author}>: This text is **{sentiment_text}**."

        compound_score = self.sia.polarity_scores(argument)['compound']
        absolute_score = abs(compound_score)

        sentiment_text = ''

        if absolute_score == 0:
            sentiment_text = 'absolutely neutral '
        elif 0.01 < absolute_score < 0.25:
            sentiment_text = 'slightly '
        elif 0.25 <= absolute_score < 0.50:
            sentiment_text = 'somewhat '
        elif 0.50 <= absolute_score < 0.75:
            sentiment_text = ''
        elif 0.75 <= absolute_score < 0.90:
            sentiment_text = 'mostly '
        elif 0.90 <= absolute_score < 1.00:
            sentiment_text = 'overwhelmingly '
        elif absolute_score == 1.00:
            sentiment_text = 'absolutely '

        if compound_score < 0:
            sentiment_text += 'negative'
        elif compound_score > 0:
            sentiment_text += 'positive'

        output = output_template.format(author=ctx.message.author.id, sentiment_text=sentiment_text)

        await ctx.send(output)
