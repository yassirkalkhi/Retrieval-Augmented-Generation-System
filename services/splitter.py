from sentence_transformers import SentenceTransformer
from sklearn.cluster import KMeans
import nltk
from nltk.tokenize import sent_tokenize

# Download necessary NLTK resources
nltk.download('punkt_tab')

class SemanticSplitterService:
    def __init__(self, model_name='all-MiniLM-L6-v2', max_chunk_size=1000, num_clusters=5):
        """
        Initialize the SemanticSplitterService.
        :param model_name: The name of the Sentence-BERT model to use.
        :param max_chunk_size: The maximum size of each chunk (in characters).
        :param num_clusters: The number of clusters to group semantically similar sentences.
        """
        self.model = SentenceTransformer(model_name)
        self.max_chunk_size = max_chunk_size
        self.num_clusters = num_clusters
    
    def split(self, text: str) -> list:
        """
        Split the provided text semantically into chunks.
        :param text: The input text to split into semantic chunks.
        :return: A list of semantic chunks.
        """
        # Step 1: Tokenize the text into sentences
        sentences = sent_tokenize(text)

        # Step 2: Use Sentence-BERT to encode sentences into embeddings
        sentence_embeddings = self.model.encode(sentences)
        if sentence_embeddings.ndim == 1:
            sentence_embeddings = sentence_embeddings.reshape(-1, 1)

        # Step 3: Apply KMeans clustering to group semantically similar sentences
        kmeans = KMeans(n_clusters=self.num_clusters, random_state=0).fit(sentence_embeddings)  

        # Step 4: Group sentences by their cluster labels
        clusters = {i: [] for i in range(self.num_clusters)}
        for idx, label in enumerate(kmeans.labels_):
            clusters[label].append(sentences[idx])

        # Step 5: Combine sentences in each cluster into chunks
        chunks = []
        for label in clusters:
            chunk = " ".join(clusters[label])
            # Ensure chunk does not exceed max_chunk_size
            if len(chunk) > self.max_chunk_size:
                # Split the chunk into smaller parts if needed
                chunks.append(chunk[:self.max_chunk_size])
                chunks.append(chunk[self.max_chunk_size:])
            else:
                chunks.append(chunk)

        return chunks