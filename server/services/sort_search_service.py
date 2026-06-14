from typing import List
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

class SortSearchService:

    def __init__(self):
        self.embedding_model = SentenceTransformer(
            'all-MiniLM-L6-v2',
        )

    def sort_service(self,query:str, search_results:List[dict]):
        query_embedding = self.embedding_model.encode(query)
        print(len(query_embedding))
        # for result in search_results:
            # result_embedding = self.embedding_model.encode(result['content'])
            # result['score'] = cosine_similarity(query_embedding, result_embedding)[0][0]
        # return sorted(search_results, key=lambda x: x['score'], reverse=True)
