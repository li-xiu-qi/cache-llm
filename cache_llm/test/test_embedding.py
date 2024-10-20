from cache_llm.config.app_config import ModelConfig
from cache_llm.config import rag_config
from cache_llm.embedding_model import EmbeddingModel
from cache_llm.types import EmbeddingInput
config = ModelConfig(
    embedding_model_name="BAAI/bge-m3",
    llm_api_configs=rag_config.guiji_api_configs,
    )
from cache_llm.chat_model import ChatModel
from cache_llm.client_manager import ClientManager




if __name__=="__main__": 
    import asyncio

    client_manager = ClientManager(config.llm_api_configs)
  
    from diskcache import Cache
    
    cache = Cache("./caches")
    embedding_model = EmbeddingModel(client_manager, cache)
    
    async def main():
        res = await embedding_model.embedding(model_input=EmbeddingInput(name=config.embedding_model_name, 
                                                                    input_content=[ "你好",  ]
                      ))
        print(res)
    asyncio.run(main())
        