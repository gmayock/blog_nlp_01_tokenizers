
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize, PunktSentenceTokenizer

example_URL_1 = "https://medicalxpress.com/news/2019-03-tavr-superior-surgery-low-risk-patients.html"

example_text_1 = "A multicenter clinical trial has found that transcatheter aortic valve replacement (TAVR) performed better than open-heart surgery in low-risk patients with severe aortic stenosis. The study found that one year after the procedure, the rate of death, stroke, or rehospitalization was significantly lower with TAVR than with surgery."

sent_tokens = sent_tokenize(example_text_1)
word_tokens = word_tokenize(example_text_1)
print("\n\n",sent_tokens,"\n\n",word_tokens,"\n\n")

example_text_2 = "\"When TAVR was introduced, it was regarded as an alternative for patients who were too sick to undergo open-heart surgery. Today's findings suggest that TAVR may be superior to surgery, even for patients with low operative risk,\" said Martin B. Leon, MD, a professor of medicine at Columbia University Vagelos College of Physicians and Surgeons, director of the Center for Interventional Vascular Therapy at NewYork-Presbyterian/Columbia University Irving Medical Center, and principal investigator of the trial."

sent_tokens_2 = sent_tokenize(example_text_2)
word_tokens_2 = word_tokenize(example_text_2)
print(sent_tokens_2,"\n\n",word_tokens_2,"\n\n")

groucho_grammar = nltk.CFG.fromstring("""
S -> NP VP
PP -> P NP
NP -> Det N | Det N PP | 'I'
VP -> V NP | VP PP
Det -> 'an' | 'my'
N -> 'elephant' | 'pajamas'
V -> 'shot'
P -> 'in'
""")

sent = ['I', 'shot', 'an', 'elephant', 'in', 'my', 'pajamas']
parser = nltk.ChartParser(groucho_grammar)
for tree in parser.parse(sent):
    tree.draw()